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

    if message.content.startswith('tropic'):
        await message.channel.send('HAHA')

    await client.process_commands(message)


@client.command(pass_context=True)
async def gel(ctx):
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        print(channel, 'HAH')
        await channel.connect()
    else:
        await ctx.message.channel.send('HAHA kanala katıl')


@client.command(pass_context = True)
async def git(ctx):
    if ctx.message.author.voice:
        server = ctx.message.guild.voice_client
        await server.disconnect()


@client.command()
@commands.has_permissions(kick_members=True)
async def tekmele(self, ctx, member: discord.Member, *, reason=None):
    await member.kick()


@client.command()
@commands.has_permissions(ban_members=True)
async def defol(self, ctx, member: discord.Member, *, reason=None):
    await member.ban()
    await ctx.channel.send(f"{user.mention} defoldu")


@client.command()
@commands.has_permissions(ban_members=True)
async def defolma(ctx, *, member):
    banned_users = await ctx.guild.bans()

    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.channel.send(f"{user.mention} artık banlı değil")


@client.command()
async def temizlik(ctx, amount=5):
    if amount > 0:
        await ctx.channel.purge(limit=amount)
        await ctx.channel.send(f"<@{ctx.message.author.id}> efendimizin emri üzerine {amount} mesaj temizlendi")
    else:
        await ctx.channel.send(f"olmaz")

client.run(botToken.TOKEN)
