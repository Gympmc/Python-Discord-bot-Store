import discord
from discord.ext import commands
import json
import os

class CogDelSlot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_role("shopy seller")
    async def delslot(self, ctx):
        await ctx.send("Please enter the slot number")

        def check(message):
            return message.author == ctx.message.author and ctx.message.channel == message.channel

        SLOTNUMBER = await self.bot.wait_for("message", timeout=20, check=check)
        slot_number = SLOTNUMBER.content

        guild_id = ctx.guild.id  # get guild id

        if slot_number == "1":
            try:
                os.remove("Guilds Data/{}/slot1.json".format(guild_id))
                await ctx.send("Slot succefuly removed !")
            except:
                await ctx.send("Invalid number !")

        elif slot_number == "2":
            try:
                os.remove("Guilds Data/{}/slot2.json".format(guild_id))
                await ctx.send("Slot succefuly removed !")
            except:
                await ctx.send("Invalid number !")

        elif slot_number == "3":
            try:
                os.remove("Guilds Data/{}/slot3.json".format(guild_id))
                await ctx.send("Slot succefuly removed !")
            except:
                await ctx.send("Invalid number !")

        elif slot_number == "4":
            try:
                os.remove("Guilds Data/{}/slot4.json".format(guild_id))
                await ctx.send("Slot succefuly removed !")
            except:
                await ctx.send("Invalid number !")

        elif slot_number == "5":
            try:
                os.remove("Guilds Data/{}/slot5.json".format(guild_id))
                await ctx.send("Slot succefuly removed !")
            except:
                await ctx.send("Invalid number !")

        elif slot_number == "6":
            try:
                os.remove("Guilds Data/{}/slot6.json".format(guild_id))
                await ctx.send("Slot succefuly removed !")
            except:
                await ctx.send("Invalid number !")

        elif slot_number == "7":
            try:
                os.remove("Guilds Data/{}/slot7.json".format(guild_id))
                await ctx.send("Slot succefuly removed !")
            except:
                await ctx.send("Invalid number !")

        elif slot_number == "8":
            try:
                os.remove("Guilds Data/{}/slot8.json".format(guild_id))
                await ctx.send("Slot succefuly removed !")
            except:
                await ctx.send("Invalid number !")

        elif slot_number == "9":
            try:
                os.remove("Guilds Data/{}/slot9.json".format(guild_id))
                await ctx.send("Slot succefuly removed !")
            except:
                await ctx.send("Invalid number !")

        elif slot_number == "10":
            try:
                os.remove("Guilds Data/{}/slot10.json".format(guild_id))
                await ctx.send("Slot succefuly removed !")
            except:
                await ctx.send("Invalid number !")

        elif slot_number != "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10":
            await ctx.send("Invalid Slot !")
        elif slot_number == str:
            await ctx.send("Please enter a correct number /!\ ")


def setup(bot):
    bot.add_cog(CogDelSlot(bot))
