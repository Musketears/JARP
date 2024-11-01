import discord, os
from discord.ext import commands
from src.other.tokens import TOKEN

intents = discord.Intents.default()
intents.message_content = True

async def load_cogs(bot):
    cog_folders = ['music', 'vpn']
    for folder in cog_folders:
        for root, _, files in os.walk(os.path.join(os.path.dirname(os.path.abspath(__file__)), "src", folder)):
            for file in files:
                if '.py' in file and not file == '__init__.py' and not '.pyc' in file:
                    cog_path = os.path.join(root, file).replace(os.path.dirname(os.path.realpath(__file__)) + os.sep,"").replace(os.sep, ".").rsplit(".py", 1)[0]
                    try:
                        await bot.load_extension(cog_path)
                    except Exception as error:
                        print(error)

class MyBot(commands.Bot):
    async def setup_hook(self):
        await load_cogs(self)
        
if __name__ == "__main__":
    my_bot = MyBot(command_prefix='?', intents=intents)
    my_bot.run(TOKEN)
