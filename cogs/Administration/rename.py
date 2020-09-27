import discord
from discord.ext import commands

class Rename(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(change_nickname=True)
    async def rename(self, ctx, user: discord.Member = None, newName = None):
      members = discord.utils.get(ctx.message.guild.members)
      if user:
            await ctx.send(userList)
            if user == user.guild.owner:
              await ctx.send('Impossible de renommer le propriétaire !')
            else:
              await user.edit(nick=newName)
              await ctx.send('{0} a été renommé {1} !'.format(user, newName))
      else:
        await ctx.send('Tu dois spécifier un nom valide à changer.')

    @rename.error
    async def rename_error(self, ctx, error):
        if isinstance(error, PermissionError):
            await ctx.send('Tu n\'as pas la permission requise pour effectuer cette action.')
        if isinstance(error, commands.BadArgument):
            await ctx.send('L\'utilisateur spécifié n\'a pas été trouvé')

def setup(client):
    client.add_cog(Rename(client))