import os, sys
import discord
import random, asyncio
import requests
from discord.ext import commands

prefix = ["da ","Da ","dA ","DA "]
intents = discord.Intents.all()
activity = discord.Game(name='ludo in da hood')
bot = commands.Bot(prefix, intents=intents, activity=activity, status=None)


# The Turn On/Off button default mode
global spam_chat_mode, spam_chat_chan
spam_chat_chan = None
spam_chat_mode = False

@bot.event
async def on_ready():
  os.system("clear")
  print(f"da homie is logged as {bot.user}")
  await asyncio.sleep(10)
  await bot.tree.sync()
  for guild in bot.guilds:
    print(f"in: {guild.name}\server id: {guild.id}")

@bot.command()
async def homie(ctx):
  await ctx.channel.send("is here")

@bot.command()
async def upgrade(ctx):
  await ctx.channel.send("Da Homie is rehoming...")
  sys.exit(0)


@bot.command()
async def sup (ctx):
  await ctx.channel.send("just homing around...")




@bot.command()
async def cat(ctx):
  def ctaget():
    data = requests.get("https://api.thecatapi.com/v1/images/search")
    return str(data.json()[0]['url'])
  daEmbed = discord.Embed(title="Da cat", description=None, color=ctx.author.color)
  daEmbed.set_image(url=ctaget())
  daEmbed.set_footer(text=ctx.author.display_name,icon_url=ctx.author.avatar)
  await ctx.reply(embed=daEmbed)
  
@bot.tree.command(name="chatspam", description="automated chat spam..!")
async def chatspam(interaction):
  global spam_chat_mode, spam_chat_chan
  if spam_chat_mode == True:
    spam_chat_mode = False
    await interaction.response.send_message("chat spam mode is now off")
  elif spam_chat_mode == False:
    spam_chat_mode = True
    spam_chat_chan = interaction.channel
    await interaction.response.send_message("chat spam mode is now on")

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return 0
  global spam_chat_mode, spam_chat_chan
  if spam_chat_mode and spam_chat_chan == message.channel:
    list = message.content.lower().split(" ")
    await message.channel.send(random.choice(list))
  await bot.process_commands(message)




def is_owner(ctx):
    return ctx.author.id == 707782594418442270,
@bot.command()
@commands.check(is_owner)
async def say(ctx, channel_id, *, message):
    channel = bot.get_channel(int(channel_id))
    if channel:
        await channel.send(message)
        await ctx.message.delete()
    else:
        await ctx.send("something wong")

@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("dA HoMIe iS nOT HoMInG")




sent_image_urls = set()

@bot.command(name="ser", aliases=["search"])
async def search_image(ctx, *, search_query: str):
    search_query_encoded = urllib.parse.quote(search_query)
    search_url = f"https://www.google.com/search?q={search_query_encoded}&tbm=isch&safe=active"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    img_tags = soup.find_all("img")

    image_urls = [img["src"] for img in img_tags if "src" in img.attrs and img["src"] not in sent_image_urls and not img["src"].endswith(".gif")]

    if image_urls:
        selected_image_url = random.choice(image_urls)
        sent_image_urls.add(selected_image_url)

        search_query_decoded = urllib.parse.unquote(search_query)
        embed = discord.Embed(color=0x9FC6F6, title=f"You searched for: {search_query_decoded}")
        embed.set_image(url=selected_image_url)

        await ctx.send(embed=embed)
    else:
        await ctx.send("wtf were you searching☠️.")























bot.run(os.environ["TOKEN"])
