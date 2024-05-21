import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f"Hemos iniciado con exito como {bot.user}")

#manualidades
@bot.command()
async def manualidades(ctx):
    ideas=["realizar ladrillos ecologicos", "hacer composta", "hacer un adorno navideño con plastico", "lampara con cucharas de plastico"]
    await ctx.send(random.choice(ideas))

#clasificación
@bot.command()
async def clasificacion(ctx,*,item:str):
    resiclabes=["carton", "botellas de plastico", "papel", "plastico"]
    no_resiclabes=["pañales", "comida"]

    if item.lower() in resiclabes:
        await ctx.send("puede ser reciclado")
    elif item.lower() in no_resiclabes:
        await ctx.send("no puede ser reciclado")
    else:
        await ctx.send("no tengo conocimiento de ellos, me falta entrenar")

bot.run("Token")
