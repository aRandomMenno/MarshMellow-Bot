import json
import random
import requests

#* idk if really important.  ↑

import os
import discord
import asyncio
from discord.ext import commands
from datetime import datetime

#! Imports up there.  ↑
#? defining the bot.  ↓

intents = discord.Intents().all()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='->', intents=intents)

#? Rest of the program down there.  ↓

now = datetime.now()
time = now.strftime("%H:%M")

@bot.event
async def on_ready():
    print(f'Bot initialize completed with user: {bot.user}')

    debugchannel = bot.get_channel(1106260528881467392)
    bot.debug_channel = bot.get_channel(debugchannel)
    await debugchannel.send(f'Bot online. Time is {time}H')

#! TEMP !

@commands.command()
async def Ping(self, ctx):
    bot_latency = round(self.bot.latency * 1000)
    await ctx.send(f"Pong! {bot_latency} ms")

#! TEMP !

async def setup_hook(self):
    async with bot():
        debugchannel = bot.get_channel(1106260528881467392)
        bot.debug_channel = bot.get_channel(debugchannel)
        await self.load_extension('Ping')
        await debugchannel.send(f"Succesfully loaded: Ping.py")
        await self.load_extension('Greeter')
        await debugchannel.send(f"Succesfully loaded: Greeter.py")


with open(r'C:\Users\Menno\OneDrive\Coding\Token.txt') as f:
    Token = f.readline()

bot.run(Token)