'''Meu Pythos Bot'''
from dotenv import load_dotenv
import os
import discord
import typing
from discord.ext import commands

load_dotenv() 


# Configs Iniciais
intents = discord.Intents.default()
intents.message_content = True 
intents.members = True
intents.presences = True
intents.reactions = True 

bot = commands.Bot(command_prefix='!', case_insensitive=True, intents=intents)
BOT_TOKEN = os.getenv('BOT_TOKEN')
print(BOT_TOKEN)

# --- IDs DE CONFIGURAÇÃO ---
ID_CARGO_AUTOMATICO = 1477300386648952843 
ID_MENSAGEM_REACAO = 1464349593511657555
ID_CANAL_BEM_VINDO = 1477081480382386331

# Dicionário de Mapeamento dos id's
CARGOS_POR_EMOJI = {
    "1438252951377285162": 1463867108369629214, # python
    "1464001086980624556": 1463867184932585556, # js
    "1464004949850722345": 1463868797508255816, # c#
    "1464014183275171972": 1463868927485673515, # html css 
    "1464000989572108410": 1463869214711349485, # c++
    "1464001138851316005": 1463872028145881149, # java
    "1464001315825778820": 1463885362794598441, # c
    "1464001709184520379": 1463872145263169629, # php
    "1464004919911518229": 1463880759738765558, # nim
    "1464006018068381931": 1463879189945122928, # cobol
    "1464001048212406394": 1463879468937515202, # go
    "1464005115949092885": 1463881966041432154, # kotlin
    "1464005846009778280": 1463887870833201286, # portugol
    "1464005094772310016": 1463869461890338910, # mysql
    "1464005044709101622": 1463871848789049429, # mongodb
    "1464013535184162951": 1463881271829725326  # oracle 
}

# --- EVENTOS ---

@bot.event
async def on_ready():
    print(f'Logado como {bot.user} (ID: {bot.user.id})')
    print('Estou pronto para começar jotta!')
    try:
        await bot.tree.sync()
    except Exception as e:
        print(f"Erro ao sincronizar: {e}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)




@bot.event
async def on_member_join(member):
    # --- Cargo Automático ---
    role = member.guild.get_role(ID_CARGO_AUTOMATICO)
    if role:
        try:
            await member.add_roles(role)
        except discord.Forbidden:
            print(f"Erro: Sem permissão para dar cargo a {member.name}")

    # --- Embed de Boas-Vindas ---
    channel = member.guild.get_channel(ID_CANAL_BEM_VINDO)
    if channel:
        embed = discord.Embed(
            title="✨ Novo Membro no Servidor!",
            description=(
                f"Seja muito bem-vindo(a), {member.mention}!\n\n"
                f"> **━━━━━━━━━━ ✧ ━━━━━━━━━━**\n\n"
                f"📜 **Leia as nossas regras:**\n"
                f" | Para manter a boa convivência, dê uma passada em <#1463882479499739350>.\n\n"
                f"> **━━━━━━━━━━ ✧ ━━━━━━━━━━**"
            ),
            color=0x3498db 
        )

        embed.set_thumbnail(url=member.display_avatar.url)
        
        # embed.set_image(url="https://i.imgur.com/vHqY7Zp.png") 

        embed.add_field(name="🔢 Membro nº", value=f"**{len(member.guild.members)}**", inline=True)
        embed.add_field(name="📅 Conta criada em", value=member.created_at.strftime("%d/%m/%Y"), inline=True)
        
        embed.set_footer(text=f"ID do usuário: {member.id} • Athos Bot")
        
        await channel.send(f"Boas-vindas {member.mention}!", embed=embed)

@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == ID_MENSAGEM_REACAO and payload.user_id != bot.user.id:
        guild = bot.get_guild(payload.guild_id)
        emoji_key = str(payload.emoji.id) if payload.emoji.is_custom_emoji() else str(payload.emoji)
        
        if emoji_key in CARGOS_POR_EMOJI:
            role = guild.get_role(CARGOS_POR_EMOJI[emoji_key])
            member = guild.get_member(payload.user_id)
            if member and role:
                try:
                    await member.add_roles(role)
                except discord.Forbidden:
                    print(f"Erro ao adicionar cargo {role.name}")

@bot.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == ID_MENSAGEM_REACAO:
        guild = bot.get_guild(payload.guild_id)
        emoji_key = str(payload.emoji.id) if payload.emoji.is_custom_emoji() else str(payload.emoji)
        
        if emoji_key in CARGOS_POR_EMOJI:
            role = guild.get_role(CARGOS_POR_EMOJI[emoji_key])
            member = guild.get_member(payload.user_id)
            if member and role:
                try:
                    await member.remove_roles(role)
                except discord.Forbidden:
                    print(f"Erro ao remover cargo {role.name}")

# --- REGISTRO ---

@bot.command()
@commands.has_permissions(administrator=True)
async def setup_registro(ctx):

    embed = discord.Embed(
        title="✨ Registro de Linguagens",
        description=(
            "**Selecione as linguagens que você utiliza ou estuda clicando nos botões abaixo para receber seus cargos automaticamente!**\n\n"
            "> **━━━━━━━━━━ ✧ ━━━━━━━━━━**\n\n"
            f"***<:python:1438252951377285162> <@&{CARGOS_POR_EMOJI['1438252951377285162']}>***\n"
            f"***<:javascript:1464001086980624556> <@&{CARGOS_POR_EMOJI['1464001086980624556']}>***\n"
            f"***<:csharp:1464004949850722345> <@&{CARGOS_POR_EMOJI['1464004949850722345']}>***\n"
            f"***<:htmlcss:1464014183275171972> <@&{CARGOS_POR_EMOJI['1464014183275171972']}>***\n"
            f"***<:cplusplus:1464000989572108410> <@&{CARGOS_POR_EMOJI['1464000989572108410']}>***\n"
            f"***<:java:1464001138851316005> <@&{CARGOS_POR_EMOJI['1464001138851316005']}>***\n"
            f"***<:clang:1464001315825778820> <@&{CARGOS_POR_EMOJI['1464001315825778820']}>***\n"
            f"***<:php:1464001709184520379> <@&{CARGOS_POR_EMOJI['1464001709184520379']}>***\n"
            f"***<:nim:1464004919911518229> <@&{CARGOS_POR_EMOJI['1464004919911518229']}>***\n"
            f"***<:cobol:1464006018068381931> <@&{CARGOS_POR_EMOJI['1464006018068381931']}>***\n"
            f"***<:go:1464001048212406394> <@&{CARGOS_POR_EMOJI['1464001048212406394']}>***\n"
            f"***<:kotlin:1464005115949092885> <@&{CARGOS_POR_EMOJI['1464005115949092885']}>***\n"
            f"***<:portugol:1464005846009778280> <@&{CARGOS_POR_EMOJI['1464005846009778280']}>***\n"
            f"***<:mysql:1464005094772310016> <@&{CARGOS_POR_EMOJI['1464005094772310016']}>***\n"
            f"***<:mongodb:1464005044709101622> <@&{CARGOS_POR_EMOJI['1464005044709101622']}>***\n"
            f"***<:oracle:1464013535184162951> <@&{CARGOS_POR_EMOJI['1464013535184162951']}>***\n\n"
            "> **━━━━━━━━━━ ✧ ━━━━━━━━━━**\n"
            "> \n"
            "> ***Após clicar, caso não tenha ganhado seu cargo peça ajuda a algum Moderador!***\n"
            "> \n"
            "**━━━━━━━━━━ ✧ ━━━━━━━━━━**"
        ),
        color=discord.Color.blue() 
    )
    

    embed.set_footer(text="Sistema de Registro Automático • Athos Bot")

    msg = await ctx.send(embed=embed) 
    
    for emoji_id in CARGOS_POR_EMOJI.keys():
        try:
            emoji = bot.get_emoji(int(emoji_id))
            if emoji:
                await msg.add_reaction(emoji)
        except Exception as e:
            print(f"Erro ao adicionar reação {emoji_id}: {e}")
            
    print(f"ID DA MENSAGEM PARA CONFIGURAR: {msg.id}")




class EmbedModal(discord.ui.Modal, title='Gerador de Mensagem Embed'):
    # Campos do formulário
    titulo = discord.ui.TextInput(
        label='Título da Embed',
        placeholder='Insira o título principal aqui...',
        required=True
    )
    
    descricao = discord.ui.TextInput(
        label='Descrição/Corpo do Texto',
        style=discord.TextStyle.paragraph,
        placeholder='O que você deseja anunciar?',
        required=True,
        max_length=2000
    )
    
    cor_hex = discord.ui.TextInput(
        label='Cor em Hexadecimal (opcional)',
        placeholder='Ex: #3498db',
        default='#3498db',
        required=False
    )
    
    imagem_url = discord.ui.TextInput(
        label='URL da Imagem (opcional)',
        placeholder='Cole o link de uma imagem (ex: imgur)',
        required=False
    )

    async def on_submit(self, interaction: discord.Interaction):
        # Lógica para converter a cor
        try:
            color_hex = self.cor_hex.value.replace('#', '')
            cor = discord.Color(int(color_hex, 16))
        except ValueError:
            cor = discord.Color.blue()

        # Criando a Embed
        embed = discord.Embed(
            title=self.titulo.value,
            description=self.descricao.value,
            color=cor
        )
        
        # Se o usuário colou um link de imagem, adiciona à embed
        if self.imagem_url.value:
            if self.imagem_url.value.startswith(("http://", "https://")):
                embed.set_image(url=self.imagem_url.value)

        embed.set_footer(text=f"Enviado por {interaction.user.display_name} • Athos Bot", icon_url=interaction.user.display_avatar.url)

        # Envia a embed no canal onde o comando foi usado
        await interaction.channel.send(embed=embed)
        # Responde apenas para quem usou o comando que deu certo
        await interaction.response.send_message("✅ Embed enviada com sucesso!", ephemeral=True)

class EmbedControl(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None) # Faz aquele botão não expirar

    @discord.ui.button(label="Abrir Editor de Embed", style=discord.ButtonStyle.success, emoji="📝")
    async def abrir_modal(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Quando o botão é clicado, ele abre o modal que já foi criado
        await interaction.response.send_modal(EmbedModal())
# COMANDOS 




@bot.command()
async def ola(ctx): await ctx.reply(f'Olá, {ctx.author.mention}')


@bot.command()
async def oi(ctx): await ctx.reply(f'Oi, tudo bem? {ctx.author.mention}')

@bot.command()
async def teste(ctx): await ctx.reply(f'Testando.. bip bop.. {ctx.author.mention}')

@bot.command()
async def suave(ctx): await ctx.reply(f'Estou suave, e você? {ctx.author.mention}')

@bot.command()
async def ajuda(ctx): await ctx.reply(f'Em que posso ajudar? {ctx.author.mention}')


@bot.command()
async def comandos(ctx):
    embed = discord.Embed(
        title="✅ Central de Comandos",
        description="Aqui estão todos os comandos disponíveis no meu sistema:",
        color=0x3498db 
    )
    
    embed.add_field(name="💬 Interação", value="`ola`, `oi`, `teste`, `suave`, `ajuda`.", inline=False)
    embed.add_field(name="🛠️ Utilidades", value="`comandos`, `avatar`, `banner`, `ping`.", inline=False)
    embed.add_field(name="🛡️ Moderação", value="`clear`, `lock`, `unlock`, `criar_embed`.", inline=False)
    
    embed.set_footer(text=f"Solicitado por {ctx.author.name}", icon_url=ctx.author.display_avatar.url)
    
    await ctx.reply(embed=embed)

@bot.command()
async def avatar(ctx, user: typing.Optional[discord.User] = None):
    user = user or ctx.author
    
    embed = discord.Embed(
        description=f"📸 Avatar de {user.mention}", 
        color=user.color
    )
    embed.set_image(url=user.display_avatar.url)
    
    await ctx.reply(embed=embed)

@bot.command()
async def banner(ctx, user: typing.Optional[discord.User] = None):
    user = user or ctx.author
    
    # fetch user utilizado para api pegar realmente o banner.
    user = await bot.fetch_user(user.id)

    if user.banner:
        embed = discord.Embed(
            description=f"✨ Banner de {user.mention}", 
            color=user.color if user.color else 0x3498db
        )
        embed.set_image(url=user.banner.url)
        await ctx.reply(embed=embed)
    else:
        await ctx.reply(f"❌ O usuário {user.mention} não possui um banner definido.")


@bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send(embed=discord.Embed(title="🔒 Canal Bloqueado", color=discord.Color.red()))

@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(embed=discord.Embed(title="🔓 Canal Desbloqueado", color=discord.Color.green()))

@bot.command()
@commands.has_permissions(manage_messages=True) 
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"🧹 Mensagens apagadas!", delete_after=5)
    
@bot.command()
async def ping(ctx):
    latency_ms = round(bot.latency * 1000)
    await ctx.send(f'Pong! Latência do Bot: **{latency_ms}ms**')
    
@bot.command(name="criar_embed")
@commands.has_permissions(administrator=True)
async def criar_embed_prefix(ctx):
    embed_aviso = discord.Embed(
        description="Clique no botão abaixo para configurar sua mensagem personalizada.",
        color=discord.Color.blue()
    )
    # Envia a mensagem com o botão
    await ctx.send(embed=embed_aviso, view=EmbedControl())
    

# Token do meu bot
bot.run(BOT_TOKEN)
