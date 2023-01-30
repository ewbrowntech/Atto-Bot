import discord
# import importlib
from integrations.YouTube.YouTube import process_download_command
# atto = importlib.import_module("Atto-API")
# atto.main.process_commands()


class AttoBotClient(discord.Client):
    async def on_ready(self):
        print("Logged in as:")
        print("Username: " + client.user.name)
        print("User ID: " + str(client.user.id))
        print("Bot Token: " + token)
        print('------')

    async def on_message(self, message):
        if message.author.id == client.user.id:  # Do not process messages sent by the bot itself
            return
        print("(" + message.guild.name + " | " + message.channel.name + ") " + message.author.name + ": " + message.content)
        if message.content.startswith('!'):  # All command message shall be formatted as ![command]
            await detect_commands(message)




# Parse messages and handle any commands present
async def detect_commands(message):
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('!download'):
        await process_download_command(message, client)


# Get Discord bot token from file
with open('tokens/discord-token', 'r') as file:
    token = file.read()


# Set the intents of the bot (what it is permitted to do)
intents = discord.Intents.default()
intents.message_content = True

# Create the bot
client = AttoBotClient(intents=intents)

# Run the bot
client.run(token)
