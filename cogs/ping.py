import discord
from discord.ext import commands


class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(str(round(float(self.bot.latency) * 1000, 2)) + "ms")


def setup(bot):
    bot.add_cog(ping(bot))
