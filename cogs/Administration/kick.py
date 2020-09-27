import discord
from discord.ext import commands

class Kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member=None):
        if user:
            await ctx.send(':boot: {}. Tu as été expulsé !'.format(user.name))
            await user.kick()
        else:
            await ctx.send('Spécifie le nom du/des utilisateur(s) que tu souhaite kicker !')
            
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, PermissionError):
            await ctx.send('Tu n\'as pas la permission requise pour effectuer cette action.')
        if isinstance(error, commands.BadArgument):
            await ctx.send('L\'utilisateur spécifié n\'a pas été trouvé')

def setup(client):
    client.add_cog(Kick(client))