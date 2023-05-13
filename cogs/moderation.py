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

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def nuke(self, ctx, count: int):
        await ctx.channel.purge(limit = count)

    #@commands.command()
    #@commands.has_permissions(kick_members = True)
    #async def kick(self, ctx, member):
        #await ctx.guild.kick(member.mention)
        #await ctx.message.add_reaction('✅')

        #punishchannel = bot.get_channel(1106885539971465226)
        #bot.debug_channel = bot.get_channel(punishchannel)
        #await punishchannel.send(f'{member.mention} was kicked by, {ctx.author.mention}!')

print("[LOG] INFO: loaded moderation.py!")

async def setup(bot):
    await bot.add_cog(moderation(bot))
