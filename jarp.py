import discord, os
from discord.ext import commands
from src.other.tokens import TOKEN, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

intents = discord.Intents.default()
intents.message_content = True

bot: commands.Bot = commands.Bot(command_prefix='?', intents=intents)

from src.music.commands.join import JoinCommand
# from src.music.commands.leave import LeaveCommand
# from src.music.commands.play import PlayCommand
# from src.music.commands.play_link import PlayLinkCommand
# from src.music.commands.playlist import PlaylistCommand
# from src.music.commands.pause import PauseCommand
# from src.music.commands.skip import SkipCommand
# from src.music.commands.queue import QueueCommand
# from src.music.commands.shuffle import ShuffleCommand
# from src.music.commands.clear import ClearCommand

#from src.music.commands import *
# for c in src.music.commands:
# bot.add_cog(c(bot))

# bot.add_cog(JoinCommand(bot))
# bot.add_cog(LeaveCommand(bot))
# bot.add_cog(PlayCommand(bot))
# bot.add_cog(PlayLinkCommand(bot))
# bot.add_cog(PlaylistCommand(bot, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET))
# bot.add_cog(PauseCommand(bot))
# bot.add_cog(SkipCommand(bot))
# bot.add_cog(QueueCommand(bot))
# bot.add_cog(ShuffleCommand(bot))
# bot.add_cog(ClearCommand(bot))

bot.load_extension('join', package='src.music.commands')

if __name__ == "__main__":
    
    bot.run(TOKEN)
