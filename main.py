import keep_alive
import manager
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands import CommandNotFound
from discord.ext.commands import BadArgument
import os

client = commands.Bot(command_prefix=commands.when_mentioned_or('.'), case_insensitive=True, help_command=None)
TOKEN = os.getenv("TOKEN")

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.Addons.{extension}')
    await ctx.send('Les addons ont été chargés !')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.Addons.{extension}')
    await('Les addons ont été déchargés !')

#Bot events

@client.event
async def on_message(message):
    await client.process_commands(message)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send('Commande non trouvée :scream: Utilise .helpme pour avoir la liste de toutes les commandes possibles.')
    return

# Addons dir
for addons in os.listdir('./cogs/Addons'):
    if(addons.endswith('.py')):
        client.load_extension(f'cogs.Addons.{addons[:-3]}')
        print(addons + ' chargé [Addons]')

# Default dir
for default in os.listdir('./cogs/'):
    if(default.endswith('.py')):
        client.load_extension(f'cogs.{default[:-3]}')
        print(default + ' chargé [Initialisation]')

# Admin dir
for admin in os.listdir('./cogs/Administration'):
    if(admin.endswith('.py')):
        client.load_extension(f'cogs.Administration.{admin[:-3]}')
        print(admin + ' chargé [Administration]')

# Fun dir
for fun in os.listdir('./cogs/Fun'):
    if(fun.endswith('.py')):
        client.load_extension(f'cogs.Fun.{fun[:-3]}')
        print(fun + ' chargé [Fun]')

# Social dir
for social in os.listdir('./cogs/Social'):
    if(social.endswith('.py')):
        client.load_extension(f'cogs.Social.{social[:-3]}')
        print(social + ' chargé [Social]')

keep_alive.keep_alive()
manager.clear()
print(TOKEN)
client.run(TOKEN)
