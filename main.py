import os, sys
import discord
import random, asyncio
from discord.ext import commands

prefix = "da "
intents = discord.Intents.all()
activity = discord.Game(name='ludo in da hood')
bot = commands.Bot(prefix, intents=intents, activity=activity, status=None)


# The Turn On/Off button default mode
global spam_chat_mode, spam_chat_chan
spam_chat_mode = None
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
  await ctx.channel.send("good night...")
  sys.exit(0)

@bot.tree.command(name="chatspam", description="automated chat spam..!")
async def chatspam(interaction):
  global spam_chat_mode, spam_chat_chan
  if spam_chat_mode == True:
    spam_chat_mode = False
    await interaction.response.send_message("chat spam mode is now off")
  elif spam_chat_mode == False:
    spam_chat_mode = True
    spam_chat_chan = interaction.channel
    await interaction.response.send_message(f"chat spam mode is now on for {spam_chat_mode.name}")

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return 0
  global spam_chat_mode, spam_chat_chan
  if spam_chat_mode and spam_chat_chan == message.channel:
    list = message.content.lower().split(" ")
    await message.channel.send(random.choice(list))
  await bot.process_commands(message)

bot.run(os.environ["TOKEN"])
