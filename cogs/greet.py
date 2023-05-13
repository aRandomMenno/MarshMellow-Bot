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

class greet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.event
    async def on_member_join(member):
        JoinChannel = bot.get_channel(1106299976360927343)
        n1 = random.randint(0,3)
        if n1 == 1:
            await JoinChannel.send(f"Welcome {member.mention} to the server!")
        elif n1 == 2:
            await JoinChannel.send(f"{member.mention} slid into the server!")
        elif n1 == 3:
            await JoinChannel.send(f"Hello {member.mention} Welcome to the server!")
        
    @bot.event
    async def on_member_leave(member):
        leaveChannel = bot.get_channel(1106299976360927343)
        n2 = random.randint(0,3)
        if n2 == 1:
            await leaveChannel.send(f"Welp wont see you again, {member.mention}")
        elif n2 == 2:
            await leaveChannel.send(f"{member.mention} slid out of the server!")
        elif n2 == 3:
            await leaveChannel.send(f"Sad, {member.mention} left the server!")

print("[LOG] INFO: loaded greet.py!")

async def setup(bot):
    await bot.add_cog(greet(bot))
