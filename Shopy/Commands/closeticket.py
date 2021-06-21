import discord
from discord.ext import commands
import discord.utils
import json

settings = json.load(open("Settings/settings.json"))
bot = commands.Bot(command_prefix=settings["prefix"])

class CogCloseTicket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_role("shopy seller")
    @commands.has_permissions(manage_channels=True, manage_messages=True)
    async def closeticket(self, ctx):
        channel = discord.TextChannel
        await ctx.channel.delete(reason="Command finish")

def setup(bot):
    bot.add_cog(CogCloseTicket(bot))