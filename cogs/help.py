import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group()
    async def helpme(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Précise sur quelle catégorie tu veux obtenir de l\'aide [admin], [fun])')

    @helpme.group()
    async def admin(self, ctx):
        adminEmbed=discord.Embed(title="Admin", description="Commandes d\'administration", color=ctx.author.color)
        adminEmbed.add_field(name=".ban [Utilisateur] [Optionnel: Raison]", value="Permet de bannir un utilisateur", inline=False)
        adminEmbed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        adminEmbed.add_field(name=".kick [Utilisateur]", value="Permet d\'expulser un utilisateur", inline=False)
        adminEmbed.add_field(name=".clear [Nombre de messages, all]", value="Permet de purger un channel", inline=False)
        adminEmbed.add_field(name=".rename [Utilisateur]", value="Permet de renommer un utilisateur", inline=False)
        adminEmbed.set_footer(text='Page d\'aide - Commandes d\'administration 1/2')
        await ctx.send(embed=adminEmbed)

    @helpme.group()
    async def fun(self, ctx):
        funEmbed=discord.Embed(title="Fun", description="Commandes Fun", color=ctx.author.color)
        funEmbed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        funEmbed.add_field(name=".say [Message à faire dire]", value="Fais dire un message défini à ButlerBot", inline=False)
        funEmbed.add_field(name=".calcul [Calcul]", value="Effectue le calcul donné, puis donne le résultat", inline=False)
        funEmbed.add_field(name=".insult", value="Permet d\insulter ButlerBot...C\'est pas très utile mais ça peut vous servir !", inline=False)
        funEmbed.add_field(name=".reverse [Message à inverser]", value="Inverse le message puis le renvoie", inline=False)
        funEmbed.set_footer(text='Page d\'aide - Commandes fun 2/2')
        await ctx.send(embed=funEmbed)

def setup(client):
    client.add_cog(Help(client))
