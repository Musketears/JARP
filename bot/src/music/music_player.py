import discord
import asyncio
import os
from src.music.sources.youtube import YTDLSource

class MusicPlayer:
    '''
    Notes TBD
    '''
    def __init__(self, bot):
        self.bot = bot
        self.init_player_attributes()

    def init_player_attributes(self):
        if not hasattr(self.bot, 'music_queue'):
            self.bot.music_queue = []
            self.bot.is_playing = False
            self.bot.current_file = ''
            self.bot.ffmpeg_path = 'ffmpeg.exe' if os.name == 'nt' else 'ffmpeg'

    async def play_url(self, ctx, url):
        voice_client = ctx.guild.voice_client
        if not voice_client:
            if ctx.author.voice:
                channel = ctx.author.voice.channel
                await channel.connect()
                voice_client = ctx.guild.voice_client
            else:
                await ctx.send("You are not connected to a voice channel.")
                return

        if self.bot.is_playing or (voice_client and voice_client.is_playing()):
            filename = await YTDLSource.from_url(url, loop=self.bot.loop)
            self.bot.music_queue.append(filename)
            await ctx.send(f"Added to queue: {filename}")
            return

        async with ctx.typing():
            self.bot.is_playing = True
            filename = await YTDLSource.from_url(url, loop=self.bot.loop)
            self.bot.current_file = filename
            voice_client.play(
                discord.FFmpegPCMAudio(executable=self.bot.ffmpeg_path, source=filename),
                after=lambda e: asyncio.run_coroutine_threadsafe(self.play_next(ctx), self.bot.loop)
            )
        await ctx.send(f'**Now playing:** {filename}')

    async def play_next(self, ctx):
        self.remove_file(self.bot.current_file)
        if self.bot.music_queue:
            voice_client = ctx.guild.voice_client
            filename = self.bot.music_queue.pop(0)
            self.bot.current_file = filename
            voice_client.play(
                discord.FFmpegPCMAudio(executable=self.bot.ffmpeg_path, source=filename),
                after=lambda e: asyncio.run_coroutine_threadsafe(self.play_next(ctx), self.bot.loop)
            )
            await ctx.send(f'**Now playing:** {filename}')
        else:
            self.bot.is_playing = False

    def remove_file(self, filename):
        if os.path.exists(filename):
            os.remove(filename)
