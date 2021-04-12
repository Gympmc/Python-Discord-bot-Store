import discord
from discord.ext import commands

class CogHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def shopy(self, ctx):
        embed_help = discord.Embed(title="Shopy, the best online store discord bot 💰", url="https://www.youtube.com")
        embed_help.add_field(name="This commands can be used by everyone", value="`s!shopy`: this help menu\n`s!buy`: buy item\n`s!showcase`: see all items for sale\n\nAdmins & shopy seller role commands:\n\n`s!setslot`: define the location of an item\n`s!delslot`: remove the location of an item\n"
        "`s!closeticket`: delete command-channel\n\nSoon:\n\n`s!blacklist`: blacklist a user of your server commands\n`s!support`: join the bot support\n`s!me`: display all your shopy-stats"
        "\n\nAdd the bot : link", inline=True)
        embed_help.set_footer(text="Shopy Bot 💰 v1.0")
        embed_help.set_thumbnail(url="https://cdn.discordapp.com/attachments/817465631678660641/817480862420697108/store.png")
        await ctx.send(embed=embed_help)

def setup(bot):
    bot.add_cog(CogHelp(bot))