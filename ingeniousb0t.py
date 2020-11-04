#All your imports
from decouple import config
from twitchio.ext import commands
import time
import sys
import random
from sfx import getsfx
from datetime import datetime
import os

#Global vars
start_time = time.time()
sound = getsfx()
now = datetime.now()
datedmy = now.strftime("%d-%m-%Y")
timehms = now.strftime("%H-%M-%S")
chatters = []

# sets up the bot from env
bot = commands.Bot(
    irc_token= config('TMI_TOKEN'),
    client_id= config('CLIENT_ID'),
    nick= config('BOT_NICK'),
    prefix=config('BOT_PREFIX'),
    initial_channels=[config('CHANNEL')]
)

@bot.event
async def event_ready():
    #Runs when bot connects to channel
    print(f"{config('BOT_NICK')} is online! at http://twitch.tv/{config('CHANNEL')}")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(config('CHANNEL'), f"/me guess who's back!") #Sends intro message

@bot.event
async def event_message(ctx):
    #Runs every time a message is sent in chat.
    global chatters
    global start_time
    global datedmy
    global timehms

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == config('BOT_NICK').lower():
        return

    #Handles bot commands
    await bot.handle_commands(ctx)

    # Timed Commands
    current_time = time.time()
    # Sends a DJ Khaled Quote every 10 minutes.
    if current_time-start_time>600:
        lines = open('djkhaled.txt').read().splitlines()
        keytosuccess = random.choice(lines)
        await ctx.channel.send(keytosuccess)
        start_time = time.time()

    # Prints chat in terminal
    print(f"{ctx.author.name}: {ctx.content}")

    #Logs chat in text file
    logger = open(f"chatlogs/log {datedmy} {timehms}.txt", "a")
    logger.write(datetime.now().strftime("%H:%M:%S") + f" {ctx.author.name}: {ctx.content}\n")
    logger.close()

    #Welcomes new chatters, exludes you
    if ctx.author.name.lower() != config('CHANNEL') and str(ctx.author.name) not in chatters:
        lines = open('greetings.txt').read().splitlines()
        greetings = random.choice(lines)
        greetings = greetings.split("ANON")
        await  ctx.channel.send(greetings[0]+ "@" + ctx.author.name+greetings[1])
        chatters.append(ctx.author.name) #Adds new chatter to list of chatters
        print("current chatters: ", chatters)

    # Recognizes keywords and sends a reply in chat
    # Some have space so that other words do not get detected
    if 'PogChamp' in ctx.content:
        await ctx.channel.send("PogChamp PogChamp PogChamp PogChamp PogChamp")
    elif 'KEKW' in ctx.content:
        await ctx.channel.send("KEKW KEKW KEKW")
    elif 'bruh' in ctx.content.lower():
        await ctx.channel.send("BRUHHHH PogChamp")
    elif 'lets go' in ctx.content.lower():
        await ctx.channel.send("LETS GOOOOOOOO KomodoHype KomodoHype KomodoHype")
    elif 'Pog' in ctx.content:
        await ctx.channel.send("Pog Pog PogU")
    

@bot.event
async def event_raw_data(data):
    # Channel Reward Points and Sound Effects, you need to require viewers to enter text to get the data
    global sound
    sound.sfx(data)

    #For testing purposes, print the raw data
    #print(data)


# BOT COMMANDS
@bot.command(name='test')
async def test(ctx):
    await ctx.send('test passed!')

@bot.command(name='discord')
async def discord(ctx):
    await ctx.send('GVNG$HIT at --> https://discord.gg/gmkEtYn')

@bot.command(name='giveaway')
async def giveaway(ctx):
    await ctx.send('No giveaways happening currently!')

@bot.command(name='youtube')
async def yt(ctx):
    await ctx.send('DEMONETIZE ME - https://www.youtube.com/ingeniousartist')

@bot.command(name='games')
async def games(ctx):
    await ctx.send('CSGO • Sea of Theives • Apex Legends • Phasmophobia • Among Us • Minecraft • Genshin Impact')


#Special Kill command to turn off bot. Only allows the streamer to turn it off. Others get a fun reply.
@bot.command(name='kill')
async def kill(ctx):
    if ctx.author.name.lower() == config('CHANNEL'):
        print('You are exiting the program.')
        await ctx.send("/me i'll be back, with subs.")
        sys.exit(0)
    else:
        await ctx.send("You aren't supposed to be doing that lol.")

if __name__ == "__main__":
    if not os.path.exists('chatlogs'): os.makedirs('chatlogs')
    bot.run()