import discord
from discord.ext import commands

class CogHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_role("shopy seller")
    async def blacklist(self, ctx, user: discord.Member = None, role=discord.Role):
        if user != None:
            await user.add_roles(role)
            await ctx.send("✅ User " + user + " has been blacklist from all the server shop !")
        else:
            await ctx.send("❌ User " + user + " isn't valid !")

def setup(bot):
    bot.add_cog(CogHelp(bot))