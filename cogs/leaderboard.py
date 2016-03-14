import discord
from discord.ext import commands
from .utils.dataIO import fileIO
import os

class Leaderboard:
    """Airenkun's temporary leaderboard cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def leaderboard(self):
        """Prints out the leaderboard"""

        bank = fileIO("data/economy/bank.json", "load")
        bank_sorted = sorted(bank.items(), key=lambda x: x[1]["balance"], reverse=True)
        topten = bank_sorted[:10]

        highscore = ""
        place = 1
        dashes = "---"
        for id in topten:
            if place > 9:
                dashes = "--"
            loop = 14 + 8 - len(str(id[1]["balance"])) - len(id[1]["name"])
            highscore += "{}{}{}".format(place,dashes,id[1]["name"])
            for i in range(1,loop+1):
                highscore += "-"
            highscore += "{}\n".format(id[1]["balance"])
            place += 1
        await self.bot.say(highscore)


def check_files():

    if not os.path.isfile("data/insult/insults.json"):
        print("bank.json is missing check your economy folder in data")

def setup(bot):
    check_files()
    n = Leaderboard(bot)
    bot.add_cog(n)
