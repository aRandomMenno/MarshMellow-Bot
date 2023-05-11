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
#? Rest of the program down there.  ↓

intents = discord.Intents().all()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='->', intents=intents)

class Greeter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        n1 = random.randint(0,3)
        channel = bot.get_channel(1106260528881467392)
        if channel is not None:
            await channel.send(f'Welcome {member.mention}.')

def setup(bot):
    bot.add_cog(Greeter(bot))
print("Debug: greeter.py")