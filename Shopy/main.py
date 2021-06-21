import discord
from discord.ext import commands
import json
import os
from discord.ext.commands import MissingRole
from discord.ext.commands import MissingPermissions
from discord.ext.commands import CommandNotFound

settings = json.load(open("Settings/settings.json"))
token = json.load(open("Settings/token.json"))

bot = commands.Bot(command_prefix=settings["prefix"])
token = token["token"]

status = settings["status"]

OWNERID = 634755612118614016

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(status))
    print("--/////////////////////////--")
    print("        Bot ONLINE !         ")
    print("--/////////////////////////--")

bot.remove_command("help")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You are missing permission(s) to run this command. You must have `shopy seller` role tu use this command !")
    elif isinstance(error, MissingRole):
        await ctx.send("You are missing permission(s) to run this command. You must have `shopy seller` role tu use this command !")
    elif isinstance(error, CommandNotFound):
        await ctx.send("Unknown command, type s!shopy.")
    else:
        raise error
@bot.event
async def on_guild_join(guild = discord.Guild):
    await guild.create_role(name="shopy seller", reason=None)
    await guild.create_role(name="shopy blacklist", reason=None)
@bot.command()
async def load(ctx, extension):
    if ctx.author.id == OWNERID:
        bot.load_extension(f'Commands.{extension}')
    else:
        await ctx.send("You don't have permission(s)")
@bot.command()
async def unload(ctx, extension):
    if ctx.author.id == OWNERID:
        bot.unload_extension(f'Commands.{extension}')
    else:
        await ctx.send("You don't have permission(s)")
for filename in os.listdir(f'./Commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'Commands.{filename[:-3]}')

bot.run(token)