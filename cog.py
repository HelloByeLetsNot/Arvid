from discord.ext import commands

class TestCog:

    def __init__(self, bot):
        self.bot = bot
        self.counter = 0

    @commands.command()
    async def add(self):
        self.counter += 1
        await self.bot.say('Counter is now %d' % self.counter)


def setup(bot):
    bot.add_cog(TestCog(bot))