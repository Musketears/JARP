from discord.ext import commands
from src.music.music_player import MusicPlayer

class PauseCommand(commands.Cog):
    '''
    Stops current song.
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='pause', help='Pause the current song')
    async def pause(self, ctx):
        voice_client = ctx.guild.voice_client
        if voice_client and voice_client.is_playing():
            voice_client.pause()
        else:
            await ctx.send("The bot is not playing anything at the moment.")
