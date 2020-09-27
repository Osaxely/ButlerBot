import discord
from discord.ext import commands
from typing import Optional

class Clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: Optional[int]):
        if ctx.invoked_subcommand is None:
            if amount != None:
                await ctx.message.delete()
                await ctx.channel.purge(limit=amount)
            else:
                await ctx.send('Spécifie le nombre de messages à supprimer (all pour purger le channel')

    @clear.group()
    @commands.has_permissions(manage_messages=True)
    async def all(self, ctx):
        await ctx.channel.purge()

def setup(client):
    client.add_cog(Clear(client))
