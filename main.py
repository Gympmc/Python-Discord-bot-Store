import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="s!")
token = "Nzc0NTM1NDA5MzE2MjY1OTg1.X6ZMTw.AA-H-Se3WSiRhpD7_3HsoDpb6pw"

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("s!start")) #
    print("--/////////////////////////--")
    print("     Lancemant du Bot ...")
    print("--/////////////////////////--")

@bot.command()
async def start(ctx):
    help_embed = discord.Embed(title="Help menu", description="**My commands :**\nOpen this menu :\n```   s!help``` "
    "\nStore Menu :\n```   s!showcase```\nAdmin menu (admins only) :\n```s!admin```")
    help_embed.set_footer(text="By Gymp_")
    await ctx.send(embed=help_embed)

slot1_name = "<none>"
slot2_name = "<none>"
slot3_name = "<none>"
slot4_name = "<none>"
slot5_name = "<none>"
slot6_name = "<none>"
slot7_name = "<none>"
slot8_name = "<none>"
slot9_name = "<none>"
slot10_name = "<none>"

slot1_price = "<none>"
slot2_price = "<none>"
slot3_price = "<none>"
slot4_price = "<none>"
slot5_price = "<none>"
slot6_price = "<none>"
slot7_price = "<none>"
slot8_price = "<none>"
slot9_price = "<none>"
slot10_price = "<none>"

slot1_icon = "<none>"
slot2_icon = "<none>"
slot3_icon = "<none>"
slot4_icon = "<none>"
slot5_icon = "<none>"
slot6_icon = "<none>"
slot7_icon = "<none>"
slot8_icon = "<none>"
slot9_icon = "<none>"
slot10_icon = "<none>"

@bot.command()
async def setslot(ctx, slot_number, name, price, icon):
    if slot_number == "1":
        slot1_name = name
        slot1_price = price
        slot1_icon = icon
        await ctx.send(slot1_name)
        await ctx.send(slot1_price)
        await ctx.send(slot1_icon)
        await ctx.send("Operation successfully completed")
        @bot.command()
        async def showcase(ctx):
            showcase_embed = discord.Embed(title="**Showcase :**", description="")
            showcase_embed.add_field(name=slot1_name, value=slot1_icon + slot1_price, inline=True)
            showcase_embed.add_field(name=slot2_name, value=slot2_icon + slot2_price, inline=True)
            showcase_embed.add_field(name=slot3_name, value=slot3_icon + slot3_price, inline=True)
            showcase_embed.add_field(name=slot4_name, value=slot4_icon + slot4_price, inline=True)
            showcase_embed.add_field(name=slot5_name, value=slot5_icon + slot5_price, inline=True)
            showcase_embed.add_field(name=slot6_name, value=slot6_icon + slot6_price, inline=True)
            showcase_embed.add_field(name=slot7_name, value=slot7_icon + slot7_price, inline=True)
            showcase_embed.add_field(name=slot8_name, value=slot8_icon + slot8_price, inline=True)
            showcase_embed.add_field(name=slot9_name, value=slot9_icon + slot9_price, inline=True)
            showcase_embed.add_field(name=slot10_name, value=slot10_icon + slot10_price, inline=True)
            await ctx.send(embed=showcase_embed)
    if slot_number == "2":
        slot2_name = name
        slot2_price = price
        slot2_icon = icon
        await ctx.send("Operation successfully completed")
    if slot_number == "3":
        slot3_name = name
        slot3_price = price
        slot3_icon = icon
        await ctx.send("Operation successfully completed")
    if slot_number == "4":
        slot4_name = name
        slot4_price = price
        slot4_icon = icon
        await ctx.send("Operation successfully completed")
    if slot_number == "5":
        slot5_name = name
        slot5_price = price
        slot5_icon = icon
        await ctx.send("Operation successfully completed")
    if slot_number == "6":
        slot6_name = name
        slot6_price = price
        slot6_icon = icon
        await ctx.send("Operation successfully completed")
    if slot_number == "7":
        slot7_name = name
        slot7_price = price
        slot7_icon = icon
        await ctx.send(slot7_name)
        await ctx.send(slot7_price)
        await ctx.send(slot7_icon)
        await ctx.send("Operation successfully completed")
    if slot_number == "8":
        slot8_name = name
        slo8_price = price
        slot8_icon = icon
        await ctx.send("Operation successfully completed")
    if slot_number == "9":
        slot9_name = name
        slot9_price = price
        slot9_icon = icon
        await ctx.send("Operation successfully completed")
    if slot_number == "10":
        slot10_name = name
        slot10_price = price
        slot10_icon = icon
        await ctx.send("Operation successfully completed")

bot.run(token)
