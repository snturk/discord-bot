import discord
from discord.ext import commands

TOKEN = 'NzYyMjc2NDMyMDg4MDA2NjY2.X3mzPw.CC6zyDcAGObSwKEzP93U4rZCOxw'

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


client.run(TOKEN)
