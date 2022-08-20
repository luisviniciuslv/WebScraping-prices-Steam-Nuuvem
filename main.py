import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix='!', case_insensitive=True)
client.remove_command('help')

for i in os.listdir('./cogs'):
  for e in os.listdir(f'./cogs/{i}'):
    if str(e).startswith('__py'):
      pass
    else:
      print('loaded ', e)
      client.load_extension(f'cogs.{i}.{e[:-3]}')

@commands.has_guild_permissions(administrator=True)
@client.command()
async def reload(ctx):
  for i in os.listdir('./cogs'):
    for e in os.listdir(f'./cogs/{i}'):
      if str(e).startswith('__py'):
        pass
      else:
        client.reload_extension(f'cogs.{i}.{e[:-3]}')
        print('loaded ', e)

client.run(os.getenv('bot_token'))