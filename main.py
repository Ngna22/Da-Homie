import os, sys
import discord
import random, asyncio
import requests
from discord.ext import commands

prefix = ["da ","Da "]
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
async def cat(ctx):
  def ctaget():
    data = requests.get("https://api.thecatapi.com/v1/images/search")
    return str(data.json()[0]['url'])
  daEmbed = discord.Embed(title="Da cat", description=None, color=0xffafbd)
  daEmbed = embed.set_image(url=ctaget())
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

import random
@bot.command()
async def commandname(ctx):
  game = ["blah", "b2", "be"]
  therandomthing = random.choice(game)
  await ctx.channel.send(therandomthing)




def is_owner(ctx):
    return ctx.author.id == 707782594418442270,1142460871365373982

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







bot.run(os.environ["TOKEN"])
