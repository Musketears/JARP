import os
import random
import string
import asyncio
import yt_dlp as youtube_dl

class YTDLSource:
    '''
    This is where we handle YouTube downloads. The from_url method provides a playable filename.

    '''
    youtube_dl.utils.bug_reports_message = lambda: ''

    ytdl_format_options = {
        'format': 'bestaudio/best',
        'restrictfilenames': True,
        'noplaylist': False,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'source_address': '0.0.0.0',
        'http_headers': {
            'User-Agent': 'Mozilla/5.0'
        }
    }

    ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
    ffmpeg_path = 'ffmpeg.exe' if os.name == 'nt' else 'ffmpeg'

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: cls.ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            data = data['entries'][0]
        og_filename = data['title'] if stream else cls.ytdl.prepare_filename(data)
        filename, file_extension = os.path.splitext(og_filename)
        filename = f"{filename}_{''.join(random.choices(string.ascii_letters + string.digits, k=8))}{file_extension}"
        os.rename(og_filename, filename)
        return filename
