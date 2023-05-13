import json
import random
import requests

#* idk if really important.  ↑

import os
import discord
import asyncio
from discord.ext import commands
from datetime import datetime

#! Imports.  ↑
#? Define bot.  ↓

intents = discord.Intents().all()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='$', intents=intents)

#? Code.  ↓

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Ping', 'P', 'p'])
    async def ping(self, ctx, member = discord.member):
        Bot_Latency = round(self.bot.latency * 1000)
        await ctx.send(f"Pong! {Bot_Latency} ms.")

print("[LOG] INFO: loaded ping.py!")

async def setup(bot):
    await bot.add_cog(ping(bot))
