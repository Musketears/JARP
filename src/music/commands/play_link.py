from discord.ext import commands
from src.music.music_player import MusicPlayer

class PlayLinkCommand(commands.Cog, MusicPlayer):
    '''
    TBD
    '''
    def __init__(self, bot):
        super().__init__(bot)

    @commands.command(name='play_link', help='To play song from YouTube link')
    async def play_link(self, ctx, url: str):
        await self.play_url(ctx, url)
