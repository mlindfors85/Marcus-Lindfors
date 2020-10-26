# Importera Discord
import asyncio
import random

import discord
from discord import Embed
from discord.ext import commands

prefix = "!"
bot = commands.Bot(command_prefix = prefix)
token = 'NzY4MDM2NzYxODE3MzE3NDA3.X46n-Q.Pu88NlqInCeTVr_u2PeVSH1xt_8'

#On Startup


@bot.event
async def on_ready():
    print ("Online")



#Events
#Random Dragning 1 till skrivet nummer efter kommando


@bot.command()
async def test(ctx):
    embed=discord.Embed(title="Lotto Kommandon", description="Välj kommando följt av antal deltagare, tex !lotto 500", color=0xeff542)
    embed.add_field(name="En Vinnare", value="!lotto", inline=False)
    embed.add_field(name="Tre Vinnare", value="!lotto3", inline=False)
    embed.add_field(name="Fem Vinnare", value="!lotto5", inline=False)
    embed.set_thumbnail(url= "http://www.livgardet.se/ext/planetstyles/h2o/store/livgardet-nya-utan-esologga.png")
    await ctx.send(embed=embed)


###########################


@bot.command()
async def lotto(ctx, num):
    embed = discord.Embed(title="Livgardets Lotteri", color=0xeff542)
    try:
        arg = random.randint(1, int(num)) 
        embed.add_field(name="Vinnare", value=(arg), inline=True)
        embed.set_thumbnail(url= "http://www.livgardet.se/ext/planetstyles/h2o/store/livgardet-nya-utan-esologga.png")
    except ValueError:
        return await ctx.send("Endast hela nummer")
    else:
        return await ctx.send(embed=embed)


#########################


@bot.command()
async def lotto3(ctx, num):
    embed = discord.Embed(title="Livgardets Lotteri", color=0xeff542)
    try:
        arg1 = random.randint(1, int(num)) 
        embed.add_field(name="Vinnare 1", value=(arg1), inline=False)
        arg2 = random.randint(1, int(num)) 
        embed.add_field(name="Vinnare 2", value=(arg2), inline=False)
        arg3 = random.randint(1, int(num)) 
        embed.add_field(name="Vinnare 3", value=(arg3), inline=False)
        embed.set_thumbnail(url= "http://www.livgardet.se/ext/planetstyles/h2o/store/livgardet-nya-utan-esologga.png")
    except ValueError:
        return await ctx.send("Endast hela nummer")
    else:
        return await ctx.send(embed=embed)


######################

@bot.command()
async def lotto5(ctx, num):
    embed = discord.Embed(title="Livgardets Lotteri", color=0xeff542)
    try:
        arg1 = random.randint(1, int(num)) 
        embed.add_field(name="Vinnare 1", value=(arg1), inline=True)
        arg2 = random.randint(1, int(num)) 
        embed.add_field(name="Vinnare 2", value=(arg2), inline=True)
        arg3 = random.randint(1, int(num)) 
        embed.add_field(name="Vinnare 3", value=(arg3), inline=True)
        arg4 = random.randint(1, int(num)) 
        embed.add_field(name="Vinnare 4", value=(arg4), inline=True)
        arg5 = random.randint(1, int(num)) 
        embed.add_field(name="Vinnare 5", value=(arg5), inline=True)
        embed.set_thumbnail(url= "http://www.livgardet.se/ext/planetstyles/h2o/store/livgardet-nya-utan-esologga.png")
    except ValueError:
        return await ctx.send("Endast hela nummer")
    else:
        return await ctx.send(embed=embed)


####################################################################################################################################



@bot.event
async def on_message(message):
    formats = ['jpg', 'png', 'gif', 'svg']
    attachments = [f for f in message.attachments if f.filename.split('.')[-1] in formats]
    if message.channel.name == 'bild' and not attachments:
        await message.delete()



bot.run(token)