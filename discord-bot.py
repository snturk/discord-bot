import discord
from discord.ext import commands
import botToken

client = commands.Bot(command_prefix='-')


@client.event
async def on_ready():
    print("Ready")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!tndr'):
        await message.channel.send('HAHA')

    await client.process_commands(message)


@client.command(pass_context=True)
async def join(ctx):
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        print(channel, 'HAH')
        await channel.connect()
    else:
        await ctx.message.channel.send('HAHA kanala katıl')


@client.command(pass_context = True)
async def leave(ctx):
    if ctx.message.author.voice:
        server = ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(self, ctx, member: discord.Member, *, reason=None):
    await member.kick()
    await log_channel.send(f"{ctx.author.name} bunu şutladı: {member.display_name}")

client.run(botToken.TOKEN)
