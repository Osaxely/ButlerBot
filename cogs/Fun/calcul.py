import discord
from discord.ext import commands

class Calcul(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def calcul(self, ctx, *, c=None):
        c = eval(c)
        await ctx.send('Le résultat est {0}'.format(c))

def setup(client):
    client.add_cog(Calcul(client))
