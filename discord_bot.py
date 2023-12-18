import discord
import emulator_control
from keys import BOT_TOKEN

intent = discord.Intents.default()
intent.message_content = True

client = discord.Client(intents=intent)

running = False

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    global running

    if message.channel.name == "discord_plays" and not message.author.bot:
        if message.content == "!start":
            running = True
            await message.channel.send(f"Inputs are being accepted")
        elif message.content == "!stop":
            running = False
            await message.channel.send(f"Inputs are being ignored")
        elif running:
            button = emulator_control.filter(message.content)

            if button:
                emulator_control.press_button(button)

client.run(BOT_TOKEN)