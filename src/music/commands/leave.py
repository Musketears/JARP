from discord.ext import commands
import asyncio
from src.music.music_player import MusicPlayer


class LeaveCommand(commands.Cog):
    '''
    Disconnects the bot from the voice channel, stops any current playback/clears queue, and removes audio files.
    '''
    def __init__(self, bot):
        self.bot = bot
        self.music_player = MusicPlayer(bot)

    @commands.command(name='leave', help='To make the bot leave the voice channel')
    async def leave(self, ctx):
        await self.music_player.remove_files(self.music_player.queue)
        self.music_player.queue.clear()
        self.music_player.is_stop = True
        voice_client = ctx.guild.voice_client
        if voice_client and voice_client.is_connected():
            await voice_client.disconnect()
            await asyncio.sleep(5)
            await self.music_player.remove_files([self.music_player.current_file])
        else:
            await ctx.send("The bot is not connected to a voice channel.")
