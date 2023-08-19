import os, sys
import discord
from discord.ext import commands

prefix = "da "
intents = discord.Intents.all()
activity = discord.Game(name='ludo in da hood')
bot = commands.Bot(prefix, intents=intents, activity=activity, status=None)


# The Turn On/Off button default mode
global spam_chat_mode
spam_chat_mode = False

@bot.event
async def on_ready():
  os.system("clear")
  print(f"da homie is logged as {bot.user}")
  for guild in bot.guilds:
    print(f"in: {guild.name}\server id: {guild.id}")

@bot.command()
async def homie(ctx):
  await ctx.channel.send("is here")

@bot.command()
async def chatspam(ctx):
  global spam_chat_mode
  if spam_chat_mode:
    spam_chat_mode = Flase
    await ctx.reply("chat spam mode is now off")
  else:
    spam_chat_mode = True
    await ctx.reply("chat spam mode is now on")

@bot.event
async def on_message(message):
  await bot.process_commands(message)
  if message.author == bot.user:
    return
  if message.content == "sleep":
    sys.exit("bye")
  if spam_chat_mode:
    list = message.content.lower().split(" ")
    await message.channel.send(random.choice(list))

bot.run(os.environ["TOKEN"])
