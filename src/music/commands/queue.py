from discord.ext import commands
from src.music.music_player import MusicPlayer

class QueueCommand(commands.Cog):
    '''
    Displays current list of songs queued, or displays if empty.
    '''
    def __init__(self, bot):
        self.bot = bot
        self.music_player = MusicPlayer(bot)

    @commands.command(name='queue', help='Display the current music queue')
    async def queue(self, ctx):
        if self.music_player.queue:
            queue_list = "\n".join(self.music_player.queue)
            await ctx.send(f"Current Queue:\n{queue_list}")
        else:
            await ctx.send("The queue is empty.")
            
async def setup(bot: commands.Bot):
    await bot.add_cog(QueueCommand(bot))