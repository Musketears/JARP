from discord.ext import commands

class ClearCommand(commands.Cog):
    '''
    Clears current queue.
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='clear', help='Clears the music queue')
    async def clear(self, ctx):
        if hasattr(self.bot, 'music_queue') and self.bot.music_queue:
            self.bot.music_queue.clear()
            await ctx.send("The music queue has been cleared.")
        else:
            await ctx.send("The queue is already empty.")

async def setup(bot: commands.Bot):
    await bot.add_cog(ClearCommand(bot))
