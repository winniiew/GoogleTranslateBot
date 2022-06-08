import discord
import googletrans
from keep_alive import keep_alive

# Create a translator object
translator = googletrans.Translator()

# The discord client
client = discord.Client()

# The token that allows client to run the script
# token = ...
token = "OTgzMjE5NzMyNzEyOTMxMzM5.GvgpnQ.1SzBHq8yz4LCMUEmDdmKWUNQImtQ2af7oy3zqg"

# Notify on console that the discord bot is ready
@client.event
async def on_ready():
  await       client.change_presence(activity=discord.Game('Translating 🗣')) 
  print("The bot is ready!")
  
# Responds to commands
@client.event
async def on_message(message):
    # Checks that the bot is not the one who sent a message
    if message.author == client.user:
        return

    # Hello test command
    if message.content.startswith("!hello"):
        await message.channel.send("Hello! {}".format(message.author.mention))

    # Command format:
    # !t <converted language> <message>
    if message.content.lower().startswith("!t "):
        # Grab the message after the command
        msg = message.content[3:]
        converted_lang = msg.split(" ")
        msg = msg[len(converted_lang[0]):]

        if converted_lang[0] != "en":
            # Directly converts English to specified language
            translated_message = translator.translate(msg, dest=converted_lang[0])
            await message.channel.send("{} -> {}".format(msg, translated_message.text))
        else:
            # Translates the language and converts it to English
            translated_message = translator.translate(msg)
            await message.channel.send("{} -> {}".format(msg, translated_message.text))

keep_alive()
client.run(token)
