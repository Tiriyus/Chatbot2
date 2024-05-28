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

@bot.command()
async def formas(ctx):
    with open('images/mem4.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def forma2(ctx):
    with open('images/mem5.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

bot.run("Token")
