from discord.ext import commands

class JoinCommand(commands.Cog):
    '''
    Controls bot joining the voice channel the user is currently in. 
    '''
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='join', help='Tells the bot to join the voice channel')
    async def join(self, ctx):
        if not ctx.author.voice:
            await ctx.send(f"{ctx.author.name} is not connected to a voice channel")
            return
        channel = ctx.author.voice.channel
        await channel.connect()

async def setup(bot: commands.Bot):
    await bot.add_cog(JoinCommand(bot))