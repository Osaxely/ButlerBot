import discord
from discord.ext import commands

class Ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='Bannie un utilisateur', description='Cette commande permet de bannir un utilisateur, utilisation: .ban @Utilisateur [Raison optionnelle]')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member = None, *,reason=None):
        if user:
            if user == ctx.message.author:
                await ctx.send('Vous ne pouvez pas vous auto-bannir ! :scream:')
            else:
                await ctx.send('{} a été banni(e) :scream: !'.format(user.name))
            if reason:
                await ctx.send('Raison: ' + reason)
            await user.ban(reason=reason)
        else:
            await ctx.send('Tu dois spécifier le nom de l\'utilisateur que tu souhaites bannir.')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, PermissionError):
            await ctx.send('Tu n\'as pas la permission requise pour effectuer cette action.')
        if isinstance(error, commands.BadArgument):
            await ctx.send('L\'utilisateur spécifié n\'a pas été trouvé')

def setup(client):
    client.add_cog(Ban(client))