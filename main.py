import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='//', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def caraoucoroa(ctx):
    moeda = ['Cara', 'Coroa']
    resultado = random.choice(moeda)
    await ctx.send(f'Resultado: {resultado}')

bot.run("COLOQUE SEU TOKEN AQUI (o discord bloqueia postagem de tokens)")
