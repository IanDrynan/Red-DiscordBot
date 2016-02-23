import discord
from discord.ext import commands
import random

class Salt:
    """Salt dispenser"""

    def __init__(self, bot):
        self.bot = bot

    async def check_salt(self, message):
        mod = self.bot.get_cog('Mod')


        if message.author.id != self.bot.user.id and message.channel.id not in mod.ignore_list["CHANNELS"]:
            if "salt" in message.content.lower():
                await self.bot.send_file(message.channel, "data/salt/salt.png")
            if "jennjenn" in message.content.lower() or "96130341705637888" in message.content:
                await self.bot.send_file(message.channel, "data/salt/cranky.jpg")
                await self.bot.send_message(message.channel, '`What.`')
            if "twerk" in message.content.lower() or "poro" in message.content.lower():
                await self.bot.send_file(message.channel, "data/salt/twerk.gif")
            if "slow" in message.content.lower() or "lag" in message.content.lower():
                await self.bot.send_file(message.channel, "data/salt/slow.png")
            if ('(╯°□°）╯︵ ┻━┻') in message.content:
                await self.bot.send_message(message.channel, "┬─┬ ノ( ゜-゜ノ)")

def setup(bot):
    n = Salt(bot)
    bot.add_listener(n.check_salt, "on_message")
    bot.add_cog(n)