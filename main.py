import discord, os, random, requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='//', intents=intents)

bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! Como posso te ajudar? (digite //comandos para ver todos os comandos disponíveis)')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh + 'h')

@bot.command()
async def caraoucoroa(ctx):
    moeda = ['Cara', 'Coroa']
    resultado = random.choice(moeda)
    await ctx.send(f'Resultado: {resultado}')

@bot.command()
async def figurinha(ctx):
    img_name = random.choice(os.listdir('M1L5/images'))
    with open(f'M1L5/images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command(aliases=['acoes'])
async def ações(ctx):
    lista_acoes = [
        "Use uma garrafa reutilizável em vez de copos e garrafas descartáveis.",
        "Feche a torneira enquanto escova os dentes ou ensaboa a louça.",
        "Tire os aparelhos eletrônicos da tomada quando não estiver usando.",
        "Separe o lixo reciclável do lixo orgânico na sua casa.",
        "Leve sua própria sacola retornável ao ir ao mercado.",
        "Reduza o tempo do banho em apenas 5 minutos."
    ]
    escolha = random.choice(lista_acoes)
    await ctx.send(f"**Ação do dia:** {escolha}")

@bot.command()
async def curiosidades(ctx):
    lista_curiosidades = [
        "Uma única garrafa plástica pode levar até 450 anos para se decompor. Ao evitar descartáveis, você impede que centenas de plásticos cheguem aos oceanos todos os anos!",
        "Uma torneira aberta gasta cerca de 12 litros de água por minuto. Fechá-la por 2 minutos ao escovar os dentes economiza mais de 700 litros por mês!",
        "Reciclar apenas 1 tonelada de papel salva cerca de 20 árvores adultas e economiza 70% da energia necessária para fazer papel novo.",
        "Sacolas plásticas são usadas por em média 12 minutos, mas ficam na natureza por séculos. Uma sacola reutilizável substitui cerca de 500 sacolas plásticas ao longo da vida.",
        "Diminuir 5 minutos no chuveiro elétrico economiza até 45 litros de água por banho e reduz bastante o gasto de energia elétrica."
    ]
    escolha = random.choice(lista_curiosidades)
    await ctx.send(f"**Você sabia?** {escolha}")

@bot.command(aliases=['poluição'])
async def poluição(ctx):
    lista_poluicao = [
        "**Lavar roupas sintéticas:** Tecidos como poliéster e nylon soltam milhares de microplásticos na água da máquina a cada lavagem, que vão direto para os rios e oceanos.",
        "**Jogar óleo de cozinha no ralo:** Apenas 1 litro de óleo que vai pelo ralo pode contaminar até 25 mil litros de água potável e impermeabilizar o solo.",
        "**Apagar e-mails e arquivos na nuvem:** Servidores que guardam fotos, vídeos e e-mails inúteis consomem quantidades gigantescas de energia elétrica e água para resfriamento.",
        "**Bitucas de cigarro no chão:** O filtro do cigarro não é feito de algodão, mas de acetato de celulose (um tipo de plástico) que libera substâncias tóxicas no solo e na água.",
        "**Recibos e notas fiscais na reciclagem:** Aquele papel térmico amarelinho contém Bisfenol (BPA) e não pode ser reciclado junto com papel comum, pois contamina o lote inteiro.",
        "**Usar esponjas de cozinha por muito tempo:** Esponjas sintéticas vão se desfazendo com o atrito da louça e liberam microplásticos invisíveis pelo ralo da pia todos os dias."
    ]
    escolha = random.choice(lista_poluicao)
    await ctx.send(f"{escolha}")

@bot.command()
async def comandos(ctx):
    linhas = [
        "- = COMANDOS = -",
        "//hello - Diz oi",
        "//heh n - Da risada varias vezes de acordo com número que você colocar",
        "//caraoucoroa - Joga uma moeda",
        "//figurinha - Envia uma figurinha aleatória",
        "//duck - Envia a foto de um pato aleatório",
        "//ações - Mostra uma atitude sustentável para o dia a dia",
        "//curiosidades - Mostra o impacto real de pequenas atitudes",
        "//poluicao - Mostra formas que você polui e nem percebe",
        "//comandos - Envia a lista de comandos atuais"
    ]
    lista = '\n'.join(linhas)
    await ctx.send(lista)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("!!SEU TOKEN!!")
