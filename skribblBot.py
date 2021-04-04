import discord
from discord.ext import commands
import win32clipboard
import aiohttp

######################################
prefix = '$'
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")
custom = []
themeWords = []
token = ""  # Bot Token
Admins = []  # Users IDs
owner = ""  # User ID
thumbnail = "https://mk0gameseverytif1pm6.kinstacdn.com/wp-content/uploads/2018/10/Skribbl-io.jpg"
color = 2507490


######################################


def custom_load():
    global custom
    f = open("custom.txt", "r")
    text = f.read()
    f.close()

    separator = "\n"
    custom = text.split(separator)


def custom_save():
    separator = "\n"
    f = open("custom.txt", "w")
    f.writelines(separator.join(custom))
    f.close()


async def getThemeWords(themeword):
    global themeWords
    themeWords = []
    url = "https://api.datamuse.com/words?topics=" + str(themeword)
    session = aiohttp.ClientSession()
    async with session.get(url) as r:
        if r.status == 200:
            js = await r.json()
            for e in js:
                themeWords.append(e['word'])
    await session.close()


async def sendDM(users):
    for user in users:
        await user.send("Skribbl Party\nSend me your custom words")


def copyToClipboard(wordlist):
    separator = ", "
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(separator.join(wordlist))
    win32clipboard.CloseClipboard()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    custom_load()


@bot.command()
async def insert(ctx, *args):
    global custom
    if isinstance(ctx.channel, discord.DMChannel):
        custom.extend(list(args))
    else:
        await ctx.send("You dumbass! Everyone can see your custom words.\n"
                       "Send the list a DM and change it up.")


@bot.command()
async def show(ctx):
    if str(ctx.author) in Admins:
        separator = ', '
        if custom:
            await ctx.send(separator.join(custom))
    else:
        await ctx.author.send("No")


@bot.command()
async def copy(ctx, arg):
    if str(ctx.author) == owner:
        copylist = custom
        if str(arg) == "theme":
            copylist = themeWords
        copyToClipboard(copylist)
    else:
        await ctx.send("No")


@bot.command()
async def save(ctx):
    if str(ctx.author) == owner:
        custom_save()
    else:
        await ctx.send("No")


@bot.command()
async def flush(ctx):
    global custom
    if str(ctx.author) == owner:
        custom = []
    else:
        await ctx.send("No")


@bot.command()
async def theme(ctx, arg):
    await getThemeWords(str(arg))


@bot.command()
async def skribbl(ctx, arg):
    voicechannel = str(arg)
    for channel in ctx.guild.voice_channels:
        if channel.name == voicechannel:
            await sendDM(channel.members)


@bot.group(invoke_without_command=True)
async def help(ctx):
    commandlist = [e.name for e in bot.commands]
    em = discord.Embed()
    em.title = "Help"
    em.description = "Hey there, Hi there, Ho there!\n" \
                     "I'm a bot that helps you with generating custom words in [skribbl.io](https://skribbl.io).\n\n" \
                     "For details, use: ```$help <command>```"
    em.set_thumbnail(url=thumbnail)
    em.colour = color
    em.add_field(name="Commands", value="\n".join(commandlist))
    await ctx.send(embed=em)


@help.command()
async def theme(ctx):
    em = discord.Embed()
    em.set_thumbnail(url=thumbnail)
    em.title = "Help - theme"
    em.description = "Updates theme words list."
    em.colour = color
    em.add_field(name="Usage", value="```$theme <theme>```")
    em.add_field(name="Example", value="```$theme duck```")
    await ctx.send(embed=em)


@help.command()
async def copy(ctx):
    em = discord.Embed()
    em.set_thumbnail(url=thumbnail)
    em.title = "Help - copy"
    em.description = "Copies the custom or theme words list to the clipboard.\n" \
                     "Only the owner of the bot can use this command."
    em.colour = color
    em.add_field(name="Usage", value="```$copy <list>```")
    em.add_field(name="Example", value="```$copy custom```\n```$copy theme```")
    await ctx.send(embed=em)


@help.command()
async def skribbl(ctx):
    em = discord.Embed()
    em.set_thumbnail(url=thumbnail)
    em.title = "Help - skribbl"
    em.description = "Sends a skribbl DM to all members in a voice channel."
    em.colour = color
    em.add_field(name="Usage", value="```$skribbl <voice channel>```")
    em.add_field(name="Example", value="```$skribbl General```")
    await ctx.send(embed=em)


@help.command()
async def save(ctx):
    em = discord.Embed()
    em.set_thumbnail(url=thumbnail)
    em.title = "Help - theme"
    em.description = "Saves custom words in a file.\n" \
                     "Only the owner of the bot can use this command."
    em.colour = color
    em.add_field(name="Usage", value="```$save```")
    await ctx.send(embed=em)


@help.command()
async def insert(ctx):
    em = discord.Embed()
    em.set_thumbnail(url=thumbnail)
    em.title = "Help - insert"
    em.description = "Insert your list of words into the custom list.\n" \
                     "If your word has space in it, use : \"your word\".\n" \
                     "You best send your list of words in a DM with me " \
                     "unless if you want to incur my wrath."

    em.colour = color
    em.add_field(name="Usage", value="```$insert <1stword> <2ndword> ...```")
    em.add_field(name="Example", value="```$insert \"hello world\" world there that foo ```")
    await ctx.send(embed=em)


@help.command()
async def flush(ctx):
    em = discord.Embed()
    em.set_thumbnail(url=thumbnail)
    em.title = "Help - flush"
    em.description = "Clears the custom words list."
    em.colour = color
    em.add_field(name="Usage", value="```$flush```")
    await ctx.send(embed=em)


@help.command()
async def show(ctx):
    em = discord.Embed()
    em.set_thumbnail(url=thumbnail)
    em.colour = color
    em.title = "Help - show"
    em.description = "Displays the custom words list."
    em.add_field(name="Usage", value="```$show```")
    await ctx.send(embed=em)


if __name__ == '__main__':
    bot.run(token)
