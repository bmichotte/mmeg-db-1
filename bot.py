import discord
from discord.ext import commands
import asyncio
from func import showCreature

bot = commands.Bot(command_prefix='?')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    
@bot.command(pass_context=True, name='creature')
async def creature(context, *args):

    res = showCreature(' '.join(args))   
    embed = discord.Embed(title=res['title'], color=0x00ff00)
    embed.add_field(name="__**Informations**__", value=res['head'], inline=True)
    embed.add_field(name="__**Caractéristiques**__", value=res['stats'], inline=True)
    embed.add_field(name="__**Lien vers la fiche**__", value=res['provider'], inline=True)
    embed.add_field(name="__**Sorts**__", value=res['spells'], inline=False)      
    embed.set_thumbnail(url=res['image'])
    embed.set_footer(text="Données fournies par mmeg-db.com")
   
       
    await bot.send_message(context.message.channel, embed=embed)

bot.run('NDY2MjUzOTQ4NTM0MzkwNzg3.DiZZ0w.0na3_HQvPL6SUBDOJek1EQdi2B8')


