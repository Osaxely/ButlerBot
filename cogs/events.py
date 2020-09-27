import discord
from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events

    @commands.Cog.listener()
    async def on_ready(self):
        print('ButlerBot v0.1 - Prêt')

def setup(client):
    client.add_cog(Events(client))
