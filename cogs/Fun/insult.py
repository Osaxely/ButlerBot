import discord
from discord.ext import commands

class Insult(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def insult(self, ctx):
        await ctx.send('https://tenor.com/view/birds-bird-funnybirds-owl-shocked-gif-4581166')

def setup(client):
    client.add_cog(Insult(client))