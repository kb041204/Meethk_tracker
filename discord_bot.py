import discord
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create bot instance with intents
intents = discord.Intents.default()
intents.message_content = True  # Required for message content access

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    
    # Send message to specific channel
    channel_id = int(os.getenv('DISCORD_CHANNEL_ID'))
    channel = bot.get_channel(channel_id)
    
    if channel:
        await channel.send("Hello! This is a test message from our bot!")
    else:
        print(f"Channel with ID {channel_id} not found")

# Run the bot with your token
bot.run(os.getenv('DISCORD_TOKEN'))