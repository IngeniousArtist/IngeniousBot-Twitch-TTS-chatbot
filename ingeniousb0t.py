# All your imports
from decouple import config
from twitchio.ext import commands
import time
import sys
import random
from speech import redeem
from datetime import datetime
import os
import requests

# Global vars
timer = time.time()
start_time = time.time()
redeem = redeem()
now = datetime.now()
datedmy = now.strftime("%d-%m-%Y")
timehms = now.strftime("%H-%M-%S")
chatters = []
colors = ['Blue','BlueViolet','CadetBlue','Chocolate','Coral','DodgerBlue','FireBrick','GoldenRod','Green','HotPink','OrangeRed','Red','SeaGreen','SpringGreen','YellowGreen']

# Sets up the bot from env
bot = commands.Bot(
    irc_token= config('TMI_TOKEN'),
    client_id= config('BEARER_ID'),
    nick= config('BOT_NICK'),
    prefix=config('BOT_PREFIX'),
    initial_channels=[config('CHANNEL')]
)

@bot.event
async def event_ready():
    # Runs when bot connects to channel
    print(f"{config('BOT_NICK')} is online! at http://twitch.tv/{config('CHANNEL')}")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(config('CHANNEL'), f"/me guess who's back!") # Sends intro message

@bot.event
async def event_message(ctx):
    # Runs every time a message is sent in chat.
    global chatters
    global timer
    global datedmy
    global timehms
    global redeem
    global colors

    # Prints chat in terminal
    print(f"{ctx.author.name}: {ctx.content}")

    # Logs chat in text file
    logger = open(f"chatlogs/log {datedmy} {timehms}.txt", "a")
    logger.write(ctx.timestamp.strftime("%H:%M:%S") + f" {ctx.author.name}: {ctx.content}\n")
    
    # Anti-Spam
    spam = open('spam.txt').read().splitlines()
    for keyword in spam:
        if keyword.lower() in ctx.content.lower():
            await ctx.channel.ban(ctx.author.name, "Banned for spamming by ingeniousb0t")
            redeem.banhammer(ctx.author.name)
            print("Banned:", ctx.author.name, "\nfor spamming:", ctx.content)
            logger.write(ctx.timestamp.strftime("%H:%M:%S") + f" BANNED {ctx.author.name} for spamming.\n")

    # Closes logger
    logger.close()

    #print(ctx.raw_data)

    # Timeout command
    if "custom-reward-id=60785c5c-2e61-4525-a458-888242be5767" in ctx.raw_data:
        await ctx.channel.timeout(ctx.content, 300, f"{ctx.author.name} timed you out")

    # BOSS FIGHT QUICK ATTACK
    if "custom-reward-id=f27cbd6d-36b2-4d95-977c-1c59566bc83d" in ctx.raw_data:
        boss = open('boss.txt').read().splitlines()
        prev_dmg = int(boss[7])
        critical = random.choice([True, False])
        quick_dmg = 42

        if int(boss[7])>int(boss[4]):
            await ctx.channel.send("/me The boss is dead! HUZZAH!")
        else:
            if critical==True:
                dmg = quick_dmg*random.randint(1,2)
                await ctx.channel.send(f"Critical! {ctx.author.name} just hit {boss[1]} with a quick attack and gave {dmg} damage!")
                boss[7] = str(prev_dmg+dmg)
                with open('boss.txt', 'w') as filehandle:
                    for listitem in boss:
                        filehandle.write('%s\n' % listitem)

            else:
                dmg = quick_dmg
                await ctx.channel.send(f"{ctx.author.name} just hit {boss[1]} with a quick attack and gave {dmg} damage!")
                boss[7] = str(prev_dmg+dmg)
                with open('boss.txt', 'w') as filehandle:
                    for listitem in boss:
                        filehandle.write('%s\n' % listitem)

    # BOSS FIGHT HEAVY ATTACK
    if "custom-reward-id=792b8863-1997-4f7e-acc6-70341d20da2a" in ctx.raw_data:
        boss = open('boss.txt').read().splitlines()
        prev_dmg = int(boss[7])
        critical = random.choice([True, False])
        heavy_dmg = 69
        
        if int(boss[7])>int(boss[4]):
            await ctx.channel.send("/me The boss is dead! HUZZAH!")
        else:
            if critical==True:
                dmg = heavy_dmg*random.randint(1,3)
                await ctx.channel.send(f"Critical! {ctx.author.name} just hit {boss[1]} with a heavy attack and gave {dmg} damage!")
                boss[7] = str(prev_dmg+dmg)
                with open('boss.txt', 'w') as filehandle:
                    for listitem in boss:
                        filehandle.write('%s\n' % listitem)

            else:
                dmg = heavy_dmg
                await ctx.channel.send(f"{ctx.author.name} just hit {boss[1]} with a heavy attack and gave {dmg} damage!")
                boss[7] = str(prev_dmg+dmg)
                with open('boss.txt', 'w') as filehandle:
                    for listitem in boss:
                        filehandle.write('%s\n' % listitem)

    # BOSS FIGHT ULT ATTACK
    if "custom-reward-id=0d8d13bc-ea71-4d92-877d-9dc5f5ed8173" in ctx.raw_data:
        boss = open('boss.txt').read().splitlines()
        prev_dmg = int(boss[7])
        critical = random.choice([True, False])
        ult_dmg = 200
        
        if int(boss[7])>int(boss[4]):
            await ctx.channel.send("/me The boss is dead! HUZZAH!")
        else:
            if critical==True:
                dmg = ult_dmg*random.randint(1,5)
                await ctx.channel.send(f"Critical! {ctx.author.name} just hit {boss[1]} with a ultimate attack and gave {dmg} damage!")
                boss[7] = str(prev_dmg+dmg)
                with open('boss.txt', 'w') as filehandle:
                    for listitem in boss:
                        filehandle.write('%s\n' % listitem)

            else:
                dmg = ult_dmg
                await ctx.channel.send(f"{ctx.author.name} just hit {boss[1]} with a ultimate attack and gave {dmg} damage!")
                boss[7] = str(prev_dmg+dmg)
                with open('boss.txt', 'w') as filehandle:
                    for listitem in boss:
                        filehandle.write('%s\n' % listitem)

    # Giveaway entry
    if "custom-reward-id=67bb4ed4-c686-432f-8f2f-8ba44b3174c4" in ctx.raw_data:
        giveaway = open('giveaway.txt','a')
        giveaway.write(f"{ctx.author.name}\n")
        giveaway.close()
        await ctx.channel.send(f"Thanks {ctx.author.name}! You just entered the giveaway!")
    
    # Channel Reward Points and Sound Effects, you need to require viewers to enter text to get the data
    redeem.points(ctx.raw_data)

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == config('BOT_NICK').lower():
        return

    # Handles bot commands
    await bot.handle_commands(ctx)

    # Timed Commands
    current_time = time.time()
    # Sends a DJ Khaled Quote every 10 minutes.
    if current_time-timer>600:
        lines = open('djkhaled.txt').read().splitlines()
        keytosuccess = random.choice(lines)
        await ctx.channel.send(keytosuccess)
        timer = time.time()
    #Changes color code for the bot
    if current_time-timer==300:
        await ctx.channel.color(random.choice(colors))

    # Welcomes new chatters, exludes you, the streamer
    if ctx.author.name.lower() != config('CHANNEL') and str(ctx.author.name) not in chatters:
        lines = open('greetings.txt').read().splitlines()
        greetings = random.choice(lines)
        greetings = greetings.split("[USERNAME]")
        await  ctx.channel.send(greetings[0]+ "@" + ctx.author.name+greetings[1])
        chatters.append(ctx.author.name) # Adds new chatter to list of chatters
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
        await ctx.channel.send("Pog Pog PogChamp")
    elif 'LUL' in ctx.content:
        await ctx.channel.send("LUL")
    elif 'discord' in ctx.content:
        await ctx.channel.send("Did someone say discord? Join our's here: https://discord.gg/UQjXeh9MRY")
    
# BOT COMMANDS

# Test command
@bot.command(name='test')
async def test(ctx):
    await ctx.send('test passed!')

# Color change
@bot.command(name='color')
async def color(ctx):
    await ctx.channel.color(random.choice(colors))

# Specs
@bot.command(name='specs')
async def specs(ctx):
    await ctx.send('Ryzen 5 3600 • RTX 2060 Super • 16GB 3200Mhz RAM • X570 Motherboard')

# Socials
@bot.command(name='socials')
async def socials(ctx):
    await ctx.send('Instagram: https://www.instagram.com/ingeniousartist/ • Discord: https://discord.gg/UQjXeh9MRY •  Youtube: https://www.youtube.com/ingeniousartist')

# Instagram command
@bot.command(name='instagram')
async def instagram(ctx):
    await ctx.send('Spam me on instagram: https://www.instagram.com/ingeniousartist/')

# Discord promo
@bot.command(name='discord')
async def discord(ctx):
    await ctx.send('GVNG$HIT at --> https://discord.gg/UQjXeh9MRY')

# Giveaways
@bot.command(name='giveaway')
async def giveaway(ctx):
    await ctx.send('No giveaways happening currently! Sorry buddy FeelsBadMan')

# Youtube promo
@bot.command(name='youtube')
async def yt(ctx):
    await ctx.send('DEMONETIZE ME - https://www.youtube.com/ingeniousartist')

# Posts current playable games
@bot.command(name='games')
async def games(ctx):
    await ctx.send('My usual games are: CSGO • Apex Legends • Phasmophobia • Rust')

# Calculates Uptime
@bot.command(name='uptime')
async def uptime(ctx):
    global start_time
    uptime = time.strftime('%H:%M:%S', time.gmtime(time.time()-start_time))
    await ctx.send(f"{config('CHANNEL')}'s stream uptime is currently {uptime}")

# Coin Flip
@bot.command(name='coinflip')
async def coinflip(ctx):
    await ctx.send(random.choice(['Heads','Tails']))

# Winning Odds
@bot.command(name='odds')
async def odds(ctx):
    await ctx.send(f"{ctx.channel.name} has "+ str(random.randint(0,100)) +"% chance of winning this")

# Airhorn sound effect. Can only be used by streamer.
@bot.command(name='airhorn')
async def airhorn(ctx):
    if ctx.author.name.lower() == config('CHANNEL'):
        os.system('Airhorn.mp3')
        await ctx.send("/me LETS GET THIS PARTY STARTED!")
    else:
        await ctx.send("You don't have the permission to play this.")

# GUCCI GANG voiceline. Can only be used by streamer.
@bot.command(name='guccigang')
async def guccigang(ctx):
    if ctx.author.name.lower() == config('CHANNEL'):
        redeem.voicecomm('guccigang')
        await ctx.send("/me GUCCIGANG GUCCIGANG GUCCIGANG")
    else:
        await ctx.send("You don't have the permission to play this.")

@bot.command(name='announcement')
async def announcement(ctx):
    if ctx.author.name.lower() == config('CHANNEL'):
        redeem.voicecomm('announcement')
        await ctx.send("/me EVERYBODY LISTEN UP")
    else:
        await ctx.send("You don't have the permission to use this.")

# Giveaway Count
@bot.command(name='giveawaycount')
async def giveawaycount(ctx):
    names = open('giveaway.txt').read().splitlines()
    await ctx.send(f"Total number of tickets entered for the giveaway is {len(names)}!")

# Giveaway my tickets
@bot.command(name='tickets')
async def tickets(ctx):
    names = open('giveaway.txt').read().splitlines()
    count = names.count(ctx.author.name)
    await ctx.send(f"{ctx.author.name}, you have entered the giveaway with {count} tickets!")

# Decide Giveaway winner
@bot.command(name='giveawaywinner')
async def giveawaywinner(ctx):
    if ctx.author.name.lower() == config('CHANNEL'):
        names = open('giveaway.txt').read().splitlines()
        winner = random.choice(names)
        await ctx.send(f"/me AND THE WINNER IS *DRUM ROLL* ... {winner}!!!")
    else:
        await ctx.send("You don't have the permission to do this.")

# Clears giveaway database
@bot.command(name='giveawayclear')
async def giveawayclear(ctx):
    if ctx.author.name.lower() == config('CHANNEL'):
        open('giveaway.txt', 'w').close()
        await ctx.send(f"/me Giveaway over. Redeem tickets now to enter for the next giveaway! Thank you!")
    else:
        await ctx.send("You don't have the permission to do this.")

# Boss HP
@bot.command(name='bosshp')
async def bosshp(ctx):
    boss = open('boss.txt').read().splitlines()
    if int(boss[7])>int(boss[4]):
        await ctx.send("/me The boss is dead. HUZZAH!")
    else:
        await ctx.send(f"{boss[1]} has {int(boss[4])-int(boss[7])}hp left out of {int(boss[4])}")

# Boss Damage
@bot.command(name='bossdmg')
async def bossdmg(ctx):
    boss = open('boss.txt').read().splitlines()
    await ctx.send(f"We gave {boss[1]} a beating of total {boss[7]}hp. NOW THAT'S A LOTTA DAMAGE!")

# Boss Lore
@bot.command(name='bosslore')
async def bosslore(ctx):
    boss = open('boss.txt').read().splitlines()
    await ctx.send(f"{boss[10]}")

# Clip channel
@bot.command(name='clip')
async def clip(ctx):
    clip_url = await bot.create_clip(config('BEARER_TOKEN'), config('AUTHOR_ID'))
    logger = open(f"clips/all clips {datedmy}.txt", "a")
    logger.write(f" {clip_url}\n")
    await ctx.send(f"Clip created! {clip_url}")

# followage
@bot.command(name='followage')
async def followage(ctx):
    url = f"https://2g.be/twitch/following.php?user={ctx.author.name}&channel={config('CHANNEL')}&format=mwdhms"
    response = requests.request("GET", url)
    await ctx.send(response.text)

# Watchtime
@bot.command(name='watchtime')
async def watchtime(ctx):
    await ctx.send(f'{ctx.author.name} has not watched {ctx.channel.name} enough! Get some popcorn and chill a bit more!')    

# Lurk command
@bot.command(name='lurk')
async def lurk(ctx):
    await ctx.send(f'Thanks for the lurk {ctx.author.name}!. Make sure to keep the volume on at least 1% to support the stream fam.')

# Subcount Command
@bot.command(name='subcount')
async def subcount(ctx):
    url = f"https://decapi.me/twitch/subcount?channel={config('CHANNEL')}"
    response = requests.request("GET", url)
    await ctx.send(f'@{ctx.author.name}, We currently have {response.text} Subscribers! KomodoHype')

# Time Command
@bot.command(name='localtime')
async def localtime(ctx):
    current_pc_time = datetime.now()
    await ctx.send(f'Time in Bangladesh is currently {current_pc_time.strftime("%I:%M %p")}')

# Special Kill command to turn off bot. Only allows the streamer to turn it off. Others get a fun reply.
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
    if not os.path.exists('clips'): os.makedirs('clips')
    bot.run()