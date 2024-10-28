from discord.ext import commands
from src.music.music_player import MusicPlayer

class SkipCommand(commands.Cog):
    '''
    Stops the current song and plays next song in queue, if it exists.
    '''
    def __init__(self, bot):
        self.bot = bot
        self.music_player = MusicPlayer(bot)

    @commands.command(name='skip', help='Skip the current song')
    async def skip(self, ctx):
        self.music_player.is_stop = False
        voice_client = ctx.guild.voice_client
        if voice_client and voice_client.is_playing():
            voice_client.stop()
        else:
            await ctx.send("The bot is not playing anything at the moment.")

async def setup(bot: commands.Bot):
    await bot.add_cog(SkipCommand(bot))