import discord
from discord.ext import commands
import json
import os

settings = json.load(open("Settings/settings.json"))
token = json.load(open("Settings/token.json"))

bot = commands.Bot(command_prefix=settings["prefix"])
token = token["token"]

status = settings["status"]

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(status))
    print("--/////////////////////////--")
    print("        Bot ONLINE !         ")
    print("--/////////////////////////--")

@bot.event
async def on_guild_join(guild = discord.Guild):
    await guild.create_role(name="shopy seller", reason=None)
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'Commands.{extension}')
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'Commands.{extension}')

for filename in os.listdir(f'./Commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'Commands.{filename[:-3]}')

bot.run(token)

