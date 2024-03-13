
import settings, discord, asyncio, os
from discord.ext import commands

bot = commands.Bot(command_prefix='$', intents=discord.Intents().all())

@bot.event
async def onReady() -> None:
    print(f'{bot.user} is now online!')

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

def main() -> None:
    asyncio.run(load())
    bot.run(token=settings.TOKEN)

if __name__ == '__main__':
    main()
