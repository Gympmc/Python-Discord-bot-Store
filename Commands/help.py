import discord
from discord.ext import commands

class CogHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def shopy(self, ctx):
        embed_help = discord.Embed(title="Commands :", description="")
        embed_help.add_field(name="All commands :", value="```s!shopy : this help menu\n\ns!setslot"
        " : sell item (require shopy seller role)\n\ns!delslot : remove slot (require shoppy seller role)\n\n"
        "s!showcase : see all items for sale\n\ns!buy : buy an item```", inline=True)
        embed_help.set_thumbnail(url="https://cdn.discordapp.com/attachments/817465631678660641/817480862420697108/store.png")
        await ctx.send(embed=embed_help)

    @commands.command()
    async def admin(self, ctx):
        admin_help = discord.Embed(title="Admin Commands :")
        admin_help.add_field(name="Defines the name, price and description of your sales slots =>",value="```t!setslot```")
        admin_help.add_field(name="Remove the requested slot =>",value="```t!delslot```")
        admin_help.add_field(name="Remove requested command channel /!\ Run in the command channel /!\ =>", value="```t!delcommand```")
        await ctx.send(embed=admin_help)

def setup(bot):
    bot.add_cog(CogHelp(bot))