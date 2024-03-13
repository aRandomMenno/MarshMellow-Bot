
from discord.ext import commands

class online(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def online(self, ctx):
        await ctx.send('working!')

async def setup(bot):
    await bot.add_cog(online(bot))
