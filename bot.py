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
ID_CARGO_AUTOMATICO = 1463870206962040985 
ID_MENSAGEM_REACAO = 1464349593511657555

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
    role = member.guild.get_role(ID_CARGO_AUTOMATICO)
    if role:
        try:
            await member.add_roles(role)
        except discord.Forbidden:
            print("Erro: Verifique a hierarquia de cargos para o cargo automático.")

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
    embed.add_field(name="🛠️ Utilidades", value="`comandos`, `avatar`, `banner`.", inline=False)
    embed.add_field(name="🛡️ Moderação", value="`clear`, `lock`, `unlock`.", inline=False)
    
    embed.set_footer(text=f"Solicitado por {ctx.author.name}", icon_url=ctx.author.display_avatar.url)
    
    await ctx.reply(embed=embed)

@bot.command()
async def avatar(ctx, user: typing.Optional[discord.User] = None):
    user = user or ctx.author
    embed = discord.Embed(title=f"Avatar de {user.name}", color=user.color)
    embed.set_image(url=user.display_avatar.url)
    await ctx.reply(embed=embed)

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
    

# Token do meu bot
bot.run(BOT_TOKEN)
