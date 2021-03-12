import discord
from discord.ext import commands
import json
import os

class CogSetslot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def setslot(self, ctx):
        guild_id = ctx.guild.id  # get guild id
        await ctx.send("Please enter the slot number")

        try:
            os.mkdir('Guilds Data/{}'.format(guild_id))
        except:
            pass

        def check(message):
            return message.author == ctx.message.author and ctx.message.channel == message.channel

        def new_article_embed(name, desc, price):
            embede = discord.Embed(title=name, description="Price : {}".format(price))
            embede.set_footer(text="Note : {}".format(desc))
            return embede

        async def new_slot():
            await ctx.send("Please enter the name")
            NAME = await self.bot.wait_for("message", timeout=30, check=check)
            slot_name = NAME.content
            await ctx.send("Please enter the description")
            DESC = await self.bot.wait_for("message", timeout=60, check=check)
            slot_desc = DESC.content
            await ctx.send("Please enter the price")
            PRICE = await self.bot.wait_for("message", timeout=30, check=check)
            slot_price = PRICE.content
            await ctx.send(embed=new_article_embed(slot_name, slot_desc, slot_price))

            guilds_data['slot'] = {}
            guilds_data['slot']['name'] = '{}'.format(slot_name)
            guilds_data['slot']['desc'] = '{}'.format(slot_desc)
            guilds_data['slot']['price'] = '{}'.format(slot_price)

        SLOTNUMBER = await self.bot.wait_for("message", timeout=20, check=check)
        slot_number = SLOTNUMBER.content

        guilds_data = {}

        if slot_number == "1":
            await new_slot()
            with open("Guilds Data/{}/slot1.json".format(guild_id), "w") as w:
                json.dump(guilds_data, w)

        elif slot_number == "2":
            await new_slot()
            with open("Guilds Data/{}/slot2.json".format(guild_id), "w") as w:
                json.dump(guilds_data, w)

        elif slot_number == "3":
            await new_slot()
            with open("Guilds Data/{}/slot3.json".format(guild_id), "w") as w:
                json.dump(guilds_data, w)

        elif slot_number == "4":
            await new_slot()
            with open("Guilds Data/{}/slot4.json".format(guild_id), "w") as w:
                json.dump(guilds_data, w)

        elif slot_number == "5":
            await new_slot()
            with open("Guilds Data/{}/slot5.json".format(guild_id), "w") as w:
                json.dump(guilds_data, w)

        elif slot_number == "6":
            await new_slot()
            with open("Guilds Data/{}/slot6.json".format(guild_id), "w") as w:
                json.dump(guilds_data, w)

        elif slot_number == "7":
            await new_slot()
            with open("Guilds Data/{}/slot7.json".format(guild_id), "w") as w:
                json.dump(guilds_data, w)

        elif slot_number == "8":
            await new_slot()
            with open("Guilds Data/{}/slot8.json".format(guild_id), "w") as w:
                json.dump(guilds_data, w)

        elif slot_number == "9":
            await new_slot()
            with open("Guilds Data/{}/slot9.json".format(guild_id), "w") as w:
                json.dump(guilds_data, w)

        elif slot_number == "10":
            await new_slot()
            with open("Guilds Data/{}/slot10.json".format(guild_id), "w") as w:
                json.dump(guilds_data, w)

        elif slot_number != "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10":
            await ctx.send("For more slots, buy Tarzan Premium ! ( t!premium )")
        elif slot_number == str:
            await ctx.send("Please enter a correct number /!\ ")


def setup(bot):
    bot.add_cog(CogSetslot(bot))

