import os
import discord
import asyncio

RESPONSE_DELAY = int(os.getenv("RESPONSE_DELAY", 2))  # default 2 detik
discord_token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Bot Discord aktif sebagai {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.reference and message.reference.message_id:
        try:
            replied_to = await message.channel.fetch_message(message.reference.message_id)
            if replied_to.author.id == client.user.id:
                await asyncio.sleep(RESPONSE_DELAY)
                await message.reply("Terima kasih sudah membalas!")
        except Exception as e:
            print(f"⚠️ Gagal membalas reply: {e}")

client.run(discord_token)
