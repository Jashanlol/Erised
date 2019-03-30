from discord.ext import commands
from random import randint


class Test_Bank(commands.Cog, name="Test Bank"):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def testbank(self, ctx, subject : str):
        """Selects random questions from a larger test bank."""

        if subject == "precalc":
            a = randint(1, 9)
            b = randint(-9, 9)
            c = randint(-9, 9)

            eq = f"Q: {a}x^2 + ({b})x + ({c})\n"
            ans = "A: quad(a, b, c)"
            ctx.send(eq + ans)


def setup(bot):
    bot.add_cog(Test_Bank(bot))
