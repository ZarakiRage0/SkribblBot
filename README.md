# SkribblBot
A discord bot to manage custom words for skribbl.io

# Motivation 
I enjoy playing skribbl.io, especially with custom words.  
However, every time we grouped up to play, we would waste time trying to get custom words from the squad and have someone managing it.  
And so, as we are always using discord to communicate while playing, I thought why not make a bot that does this work for us.  
Also, it was an opportunity to see how discord bots were made.  

# About
The bot can generate custom &/or theme words for you to use in [skribbl.io](https://skribbl.io).  
Hence, the bot has commands like ```$insert```, ```$theme```.  
To check the custom words, use the command ```$show custom```.  
The words are stored in a list. And so you can save these words for another day through ```$save``` or you can clear the list using ```$flush```.  
Side note, when you run the bot, it loads ```custom.txt``` into the custom words' list.  
To keep the words list a secret from everyone, ```$copy``` is used to copy the list directly into your clipboard.  

For further details on the commands, use the ```$help``` command.

# Before You run it

## Libraries

You should install these libraries:
 
- [discord.py](https://discordpy.readthedocs.io/en/stable/) for managing the bot
- [aiohttp](https://docs.aiohttp.org/en/stable/) fot getting theme words
- [win32clipboard](http://timgolden.me.uk/pywin32-docs/win32clipboard.html) for copying the custom/theme words into your clipboard


## Variables
You would also need to set:

- token: the bot's token.
- Admins: list of users' Ids who can invoke the ```$show``` command.
- owner: user's Id of the one running the bot.

And now, you are set to go.  
Just run the bot's script.
