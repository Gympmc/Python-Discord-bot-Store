import discord
from discord.ext import commands
import json
import os

class Showcase(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def showcase(self, ctx):

        guild_id = ctx.guild.id

        showcase_embed = discord.Embed(title="Showcase :", description="All items for sale !")
        showcase_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/817465631678660641/817480862420697108/store.png")
        try:
            for filename in os.listdir("Guilds Data/{}".format(guild_id)):
                if filename.endswith(".json"):
                    with open("Guilds Data/{}/{}".format(guild_id, filename)) as f:
                        data = json.load(f)
                        data2 = data.get("slot")
                        name = data2.get("name")
                        desc = data2.get("desc")
                        price = data2.get("price")
                    showcase_embed.add_field(name="{}".format(filename[:-5]), value="```{}\n\n{}\n\nPrice : {}```".format(name, desc, price), inline=True)
                    showcase_embed.set_footer(text="for add a slot (max 10), use t!setslot")
            await ctx.send(embed=showcase_embed)
        except FileNotFoundError:
            error_embed = discord.Embed(title="Error", description="The requested location has not been defined by the sellers, if you are a seller, type s!shopy or s!setslot.")
            error_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/817465631678660641/817480862420697108/store.png")
            await ctx.send(embed=error_embed)



def setup(bot):
    bot.add_cog(Showcase(bot))