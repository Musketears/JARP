from discord.ext import commands
from src.music.sources.spotify import SpotifyAPI
from src.music.music_player import MusicPlayer
from youtube_search import YoutubeSearch

class PlaylistCommand(commands.Cog, MusicPlayer):
    def __init__(self, bot, spotify_client_id, spotify_client_secret):
        super().__init__(bot)
        self.spotify_api = SpotifyAPI(spotify_client_id, spotify_client_secret)

    @commands.command(name='playlist', help='Play a Spotify playlist, paste the share link after')
    async def playlist(self, ctx, link):
        playlist_uri = link.split("/")[-1].split("?")[0]
        tracks = self.spotify_api.get_playlist_tracks(playlist_uri)
        for track in tracks:
            query = f"{track['name']} by {', '.join(artist['name'] for artist in track['artists'])}"
            await self.play_query(ctx, query=query)

    async def play_query(self, ctx, *, query: str):
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            if results:
                url_suffix = results[0]['url_suffix']
                url = "https://www.youtube.com" + url_suffix
                await self.play_url(ctx, url)
            else:
                await ctx.send(f"No results found for '{query}'.")
        except Exception as e:
            await ctx.send(f"An error occurred while playing '{query}': {e}")

async def setup(bot: commands.Bot):
    await bot.add_cog(PlaylistCommand(bot))