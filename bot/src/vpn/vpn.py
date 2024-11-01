from discord.ext import commands
import subprocess

class VpnCommand(commands.Cog):
    '''
    Connects the vpn to a new region
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='vpn', help='Connects the vpn to a new region')
    async def clear(self, ctx):
        result = subprocess.run(["nordvpn", "connect"], capture_output=True, text=True)
        await self.bot.connect(reconnect=True)
        await ctx.send(result.stdout if result.stdout else result.stderr)

async def setup(bot: commands.Bot):
    await bot.add_cog(VpnCommand(bot))
