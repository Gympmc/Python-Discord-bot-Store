import discord
from discord.ext import commands
import json
import os

settings = json.load(open("Settings/settings.json"))
bot = commands.Bot(command_prefix=settings["prefix"])

class CogBuy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def buy(self, ctx):
        guild = discord.Guild
        """
        def check(message):
            return message.author == ctx.message.author and ctx.message.channel == message.channel

        await ctx.send("Please enter the slot number you want to buy (ex : slot6)")
        slot = await bot.wait_for("message", timeout=30, check=check)
        slot_number = slot.content
        """

        # await guild.create_role(self="none", name="{}".format(ctx.author.id), reason="none")

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True)
        }

        with open("Settings/ticket-count.json") as f:
            data = json.load(f)
        ticket_number = int(data["count"])
        ticket_number += 1
        await ctx.guild.create_text_channel(name='AU DD', overwrites=overwrites)

def setup(bot):
    bot.add_cog(CogBuy(bot))