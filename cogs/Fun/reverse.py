import discord
from discord.ext import commands

class ReverseText(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def Reverse(self, ctx, *, words):
        def reverse(s):
            return s[::-1]
        await ctx.send(reverse(words))

def setup(client):
    client.add_cog(ReverseText(client))