
from discord.ext import commands

class punish(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ban(self, ctx):
        await ctx.send('Pong!')
        
    @commands.command()
    async def kick(self, ctx):
        await ctx.send('Pong!')
        
    @commands.command()
    async def mute(self, ctx):
        await ctx.send('Pong!')

async def setup(bot):
    await bot.add_cog(punish(bot))
    print(f'punish.py was loaded successfully')