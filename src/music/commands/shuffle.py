from discord.ext import commands
import random
from src.music.music_player import MusicPlayer

class ShuffleCommand(commands.Cog):
    '''
    Attempts to shuffle songs played from the queue.
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='shuffle', help='Shuffles the music queue')
    async def shuffle(self, ctx):
        if hasattr(self.bot, 'music_queue') and self.bot.music_queue:
            random.shuffle(self.bot.music_queue)
            await ctx.send("The music queue has been shuffled.")
        else:
            await ctx.send("The queue is empty; nothing to shuffle.")

def setup(bot):
    bot.add_cog(ShuffleCommand(bot))
