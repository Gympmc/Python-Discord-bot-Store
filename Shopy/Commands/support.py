import discord
from discord.ext import commands

class CogSupport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def support(self, ctx):
        support_embed = discord.Embed(title="Join the support", description="", url="https://discord.gg/JW76uzbarU")
        support_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/817465631678660641/817480862420697108/store.png")
        support_embed.set_footer(text="Shopy Bot 💰 v1.1")
        await ctx.send(embed=support_embed)

def setup(bot):
    bot.add_cog(CogSupport(bot))