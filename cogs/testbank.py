from discord.ext import commands
from random import randint
from random import getrandbits
from cogs.utils.formulas import quad


class Test_Bank(commands.Cog, name="Test Bank"):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def testbank(self, ctx, subject : str):
        """Selects random questions from a larger test bank."""

        if subject == "precalc":
            topic = randint(1, 3)
            
            for i in range(5):
                a = randint(1, 9)
                b = randint(-9, 9)
                c = randint(-9, 9)

                eq = f"Q: Find the zeros of the quadratic equation {a}x^2 + ({b})x + ({c})\n"
                ans = f"A: {quad(a, b, c)}"
                await ctx.send(eq + ans)
        elif subject == "physics":
            f = open("cogs/utils/Testbankpdf.txt", "r")
            n = 0
            split_lines = f.read().split("\n\n")
            output = ""

            for question_n in split_lines:
                if n == 5:
                    break
                if bool(getrandbits(1)):
                    output += question_n
                    output += '\n'
                    n += 1
                
            
            await ctx.send(output)
            f.close()


def setup(bot):
    bot.add_cog(Test_Bank(bot))
