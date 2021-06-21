import discord
from discord.ext import commands
import discord.utils
import json
import os

settings = json.load(open("Settings/settings.json"))
bot = commands.Bot(command_prefix=settings["prefix"])

class CogBuy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def buy(self, ctx, slotname):

        valid_slots = []
        for slot_name in os.listdir("Guilds Data/{}".format(ctx.guild.id)):
            if slot_name.endswith(".json"):
                valid_slots.append(slot_name[:-5])

        print(valid_slots)

        if slotname in valid_slots:
            print("valid slot ok")

            with open("Guilds Data/{}/{}.json".format(ctx.guild.id, slotname)) as f:
                data = json.load(f)
                data2 = data.get("slot")
                name = data2.get("name")
                desc = data2.get("desc")
                price = data2.get("price")

            print(ctx.guild.roles)
            from discord.utils import get
            role_name = "shopy seller"
            shopy_seller_role = get(ctx.guild.roles, name=role_name)
            print(shopy_seller_role)

            perms = {
                ctx.message.guild.default_role: discord.PermissionOverwrite(view_channel=False),
                ctx.message.author: discord.PermissionOverwrite(view_channel=True, read_messages=True,
                                                                read_message_history=True, send_messages=True),
                shopy_seller_role: discord.PermissionOverwrite(view_channel=True, read_messages=True)
            }

            guild = ctx.message.guild
            channel = await guild.create_text_channel('shopy-command-{}'.format(ctx.message.author.name),
                                                      overwrites=perms)
            print("text channel create")

            close_embed = discord.Embed(title="Shopy-command of {}".format(ctx.message.author.name),
                                        description="buyer: <@{}>".format(ctx.message.author.id))
            close_embed.add_field(name="{}".format(slotname), value="```name: {}\ndescription: {}\nprice: {}```".format(name, desc, price))
            close_embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/817465631678660641/817480862420697108/store.png")
            close_embed.set_footer(text="**Type s!closeticket <name of the channel> to close !**")
            await channel.send(embed=close_embed)
            await channel.send("@everyone")

            command_confirmed = discord.Embed(title="Command confirmed", description="<@{}>, your order has been confirmed, you can view it in your command channel !".format(ctx.author.id))
            command_confirmed.set_thumbnail(url="https://cdn.discordapp.com/attachments/817465631678660641/817480862420697108/store.png")
            await ctx.send(embed=command_confirmed)

        else:
            await ctx.send("This slot isn't valid, please enter a valid slot ! (s!showcase) <@{}>".format(ctx.message.author.id))



def setup(bot):
    bot.add_cog(CogBuy(bot))