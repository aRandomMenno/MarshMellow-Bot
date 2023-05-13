import os
import time
import discord
import asyncio
from discord.ext import commands, tasks
from datetime import datetime

#! Imports.  ↑
#* Define bot.  ↓

intents = discord.Intents().all()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='$', intents=intents)

#? Code.  ↓

@tasks.loop(seconds = 10)
async def status():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name= "help for commands. Contact aRandomMenno#3143 if you need anything."))

@bot.event
async def on_ready():
    print('[LOG] INFO: Bot initialize completed')
    status.start()

    debugchannel = bot.get_channel(1106260528881467392)
    bot.debug_channel = bot.get_channel(debugchannel)
    now = datetime.now()
    time = now.strftime("%H:%M")
    await debugchannel.send(f'Bot online. Time is {time}H')

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def start():
    await load()
    with open(r'../../Token.txt') as f:
        Token = f.readline()
    await bot.start(Token)

asyncio.run(start())
