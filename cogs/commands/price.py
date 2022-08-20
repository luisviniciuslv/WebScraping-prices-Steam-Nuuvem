import asyncio

import discord
from discord.ext import commands
from utils.get_price_nuuvem import get_price_nuuvem
from utils.get_price_steam import getItemSteam, itensSugestion


class Galo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def price(self, ctx, *, name: str):
        embed = discord.Embed(title="Carregando...", description=f"| **Aguarde enquanto nossos**\n| **servidores processam seu pedido!**", color=0x5662F6)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/902225085245563021/1005553602242289725/unknown.png")

        msg = await ctx.channel.send(embed=embed)

        embed = discord.Embed(title="Você quis dizer qual jogo?", color=0xC2FA93) 
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/902225085245563021/1005555265288024094/unknown.png")

        reactions = []
        names = []

        itens = itensSugestion(name)[:3]

        if len(itens) == 0:
            await ctx.send("Não encontramos nenhum jogo com esse nome")
            return

        for name, reaction in zip(itensSugestion(name)[:3], ['1️⃣', '2️⃣', '3️⃣']):
            embed.add_field(name=f'{reaction} {name}', value='** **', inline=False)
            reactions.append(reaction)
            names.append(name)

        await msg.edit(embed=embed)

        for i in reactions:
            await msg.add_reaction(i)

        def check(reaction, user):
            return user.id == ctx.author.id and str(reaction.emoji) in reactions

        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=20.0, check=check)

            for escolha, name in zip(reactions, names):
                if str(escolha) == str(reaction):
                    dataSteam = getItemSteam(name)
                    dataNuuvem = get_price_nuuvem(name)

                    embed = discord.Embed(title=dataSteam['name'], color=0x5662F6)
                    embed.set_image(url=dataSteam['image'])

                    embed.add_field(name='Steam', value=f'[{dataSteam["price"]}]({dataSteam["url"]})', inline=False)
                    embed.add_field(name='Nuuvem', value=f'[{dataNuuvem["price"]}]({dataNuuvem["url"]})', inline=False)
        
                    await msg.clear_reactions()
                    await msg.edit(embed=embed)

        except asyncio.TimeoutError:
            return await msg.delete()

def setup(client):
  client.add_cog(Galo(client))
