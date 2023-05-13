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

class template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

print("[LOG] INFO: loaded template.py!")

async def setup(bot):
    await bot.add_cog(template(bot))
