import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import os

token = os.getenv("DISCORD_BOT_TOKEN")

client = commands.Bot(command_prefix='-')

players = {}

botManual = '''
        :pear: HAHA komutlar şöyle;
        
        :coconut:   **-temizle** [komut]: komut eğer sayı ise o sayı kadar *mesajı kanaldan temizle*, komut olarak **kanal** yazılırsa kanalı temizler, sayı yazılmazsa 5 mesaj temizler
        
            
        :avocado:    **-gel**: kanala *çağır*
            
        :cucumber:    **-git**: kanaldan *git*
            
        :cherries:    **-oynat [video adı]**: kanalda iken *youtube videosu çal*
            
        :carrot:    **-tekmele [biri]**: birini sunucudan *at*
            
        :potato:    **-defol [biri]**: birini sunucudan *yasakla*
            
        :tomato:    **-defolma [isim#etiket]**: birinin *yasağını kaldır*
             
                                   '''

@client.event
async def on_ready():
    print("Ready")

<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes

@client.event
async def on_message(message):
    channel = message.channel
    content = message.content
    if message.author == client.user:
        return

    if str(channel) == "🍇tropic-komut🍇":
        if not message.author == "tropic" and not content.startswith("-"):
            await message.channel.purge(limit=1)
            await channel.send('lütfen, sadece komut')
    elif content.startswith("-") and not content.startswith("-temizle"):
        await message.channel.purge(limit=1)
        await channel.send('bura yeri değil, 🍇tropic-komut🍇 kanalına bekleriz')



    await client.process_commands(message)


@client.command(pass_context=True)
async def komutlar(ctx):
    await ctx.message.channel.send(botManual)

@client.command(pass_context=True)
async def gel(ctx):
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.message.channel.send('HAHA önce kanala katıl')


@client.command(pass_context=True)
async def git(ctx):
    if ctx.message.author.voice:
        server = ctx.message.guild.voice_client
        await server.disconnect()
    else:
        await ctx.message.channel.send('tamam da nerden?')


@client.command(pass_context=True)
async def oynat(ctx):
    await gel(ctx)
    key = ctx.message.content

    url = key.replace("-oynat ", "")

    YDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist': 'False', 'default_search': 'auto'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)

        if str(url).startswith('http'):
            URL = info['formats'][0]['url']
        else:
            URL = info['entries'][0]['formats'][0]['url']

        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
    else:
        await ctx.send("dur bi")
        return


@client.command(pass_context=True)
async def durdur(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.pause()
    await ctx.message.add_reaction('🍳')


@client.command(pass_context=True)
async def devamke(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.resume()
    await ctx.message.add_reaction('🍦')


@client.command(pass_context=True)
async def bitir(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    await ctx.message.add_reaction('🥓')


@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def tekmele(ctx, member: discord.Member):
    await member.kick()
    await ctx.message.channel.send(f'<@{member.id}> efendimiz tarafından tekmelendi')


@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def defol(ctx, member: discord.Member):
    await ctx.send(f"{member} defoldu")
    await member.ban()


@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def defolma(ctx, *, member):
    banned_users = await ctx.guild.bans()

    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.channel.send(f"{user.mention} artık banlı değil")


@client.command(pass_context=True)
@commands.has_permissions(change_nickname=True)
async def takmaAd(ctx, member: discord.Member, newNick):
    await ctx.channel.send(f'<@{member.id}>, efendimiz sana **{newNick}** ismini layık gördü')
    await member.edit(nick=newNick)


@client.command()
async def temizle(ctx, amount="5"):
    if str(amount) == "kanal":
        msgToDeleteCount = 1
        async for i in ctx.channel.history():
            msgToDeleteCount += 1

        await ctx.channel.purge(limit=msgToDeleteCount)
    else:
        if int(amount) > 0:
            await ctx.channel.purge(limit=int(amount))
            await ctx.channel.send(f"<@{ctx.message.author.id}> efendimizin emri üzerine {amount} mesaj temizlendi")
        else:
            await ctx.channel.send(f"olmaz")



client.run(token)
