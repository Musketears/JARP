from discord.ext import commands
from youtube_search import YoutubeSearch
from src.music.music_player import MusicPlayer

class PlayCommand(commands.Cog, MusicPlayer):
    '''
    Allows user to play a song given a search query. Retrieves the first result and plays it.
    '''
    def __init__(self, bot):
        super().__init__(bot)

    @commands.command(name='play', help='To play song from YouTube search')
    async def play(self, ctx, *, query: str):
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            if results:
                url_suffix = results[0]['url_suffix']
                url = "https://www.youtube.com" + url_suffix
                await self.play_url(ctx, url)
            else:
                await ctx.send("No results found for your query.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

async def setup(bot: commands.Bot):
    await bot.add_cog(PlayCommand(bot))