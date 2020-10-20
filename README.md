## IngeniousBot: The text to speech Twitch Chatbot you needed!

![Demo](https://github.com/IngeniousArtist/IngeniousBot-Twitch-TTS-chatbot/blob/main/IngeniousBot.png)

>**This Bot has been built with a base from [Barebones Twitch Bot](https://github.com/NinjaBunny9000/barebones-twitch-bot) by @NinjaBunny9000.**
>**Big thanks to her, do check her out: [NinjaBunny9000](https://github.com/NinjaBunny9000) - _Author, Project Manager_ - [Twitch](https://twitch.tv/ninjabunny9000) //  [Twitter](https://twitter.com/ninjabunny9000)**

If you liked using this bot, give it a ✨ and follow me on - [Twitch](https://www.twitch.tv/ingeniousartist) // [Twitter](https://twitter.com/ShahriyerShuvo)
Join our [Discord!](https://discord.gg/gmkEtYn) for some fun times.

## Features
- Sends an introduction message and a goodbye message
- Responds to basic greetings, PogChamps and KEKWs
- Does Text-to-Speech(TTS) on highlighted messages
- Calls you out on Channel point rewards
- Has a self-destruct kill command for the streamer
- Spams DJ Khaled quotes every 10 minutes in chat
- Speaks in Google Translate and fluent Dothraki (jk)

## Pre-installing
- Use a secondary account for the bot. It is much easier that way.
- Login to your bot account on twitch
- Go to [Twitch TMI](https://twitchapps.com/tmi/) to get your oauth token
- Then register your app on [Twitch Developers](https://dev.twitch.tv/console/apps) and copy the Client ID of your app.
- You must put these in your `.env` file for the bot to work
- Open the `runbot.bat` file in your editor and put the path to `python3` and the path to `ingeniousb0t.py` inside.

## Installing
- Clone the repo and unzip
- Open terminal in the directory and run `pip install -r requirements.txt`
- Copy & rename `.env-example` to `.env`
- Put in all the secrets in your `.env` file and save
- run `python3 ingeniousb0t.py` or edit and use the batch file `runbot.bat` to run the bot
- type `!test` in your twitch chat to check if the bot works


## Events

There are 2 events that are used in the code right now.. `on_ready`, `on_event`.

### on_ready
This executes when the bot comes online, and will print out to the console. 
```python
@bot.event
async def event_ready():
    # Runs when bot connects to channel
    print(f"{config('BOT_NICK')} is online! at http://twitch.tv/{config('CHANNEL')}")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(config('CHANNEL'), f"/me guess who's back!") #Sends intro message
```

### event_message
This function executes once per event (or message) sent. You can make it handle all kinds input from chat.

```python
@bot.event
async def event_message(message):
    # Prints chat in terminal
    print(f"{ctx.author.name}: {ctx.content}")
    # Handles commands
    await bot.handle_commands(message)
```

### event_raw_data
This function is the raw data version of `event_message` and also executes once per event (or message) sent. I am using it for interacting with channel reward points and Text-to-Speech(TTS). For TTS commands to function properly, please put your default audio player settings to close automatically when the audio is finished playing.

```python
@bot.event
async def event_raw_data(data):
    # Prints raw chat data in terminal
    print(data)
```

## Commands

You can make the bot handle all sorts of commands.

### Test command
This function tests to see if the bot is working properly. Sends a reply in chat.

```python
@bot.command(name='test')
async def test(ctx):
    await ctx.send('test passed!')
```

### Kill command
This function is a special kill command which turns off the bot from chat. Only the streamer can make the bot go away.

```python
@bot.command(name='kill')
async def kill(ctx):
    if ctx.author.name.lower() == config('CHANNEL'):
        print('You are exiting the program.')
        await ctx.send("/me i'll be back, with subs.")
        sys.exit(0)
    else:
        await ctx.send("You aren't supposed to be doing that lol.")
```

You can find more info in [TwitchIO's official documentation](https://twitchio.readthedocs.io/en/rewrite/twitchio.html).
