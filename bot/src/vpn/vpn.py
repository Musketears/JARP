from discord.ext import commands
import subprocess, time, os

class VpnCommand(commands.Cog):
    '''
    Connects the vpn to a new region
    '''
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.command(name='vpn', help='Connects the vpn to a new region')
    async def clear(self, ctx):
        await ctx.send("Reconnecting to vpn, this will take minumum 15 seconds. the bot will not respond till it has connected")
        result = subprocess.run(["nordvpn", "connect"], capture_output=True, text=True)
        while True:
            time.sleep(1)
            try:
                await ctx.send(result.stdout if result.stdout else result.stderr)
                break
            except:
                tries+=1

async def setup(bot: commands.Bot):
    await bot.add_cog(VpnCommand(bot))
