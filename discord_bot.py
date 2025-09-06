import discord
import os
from dotenv import load_dotenv
from classes import meethk_scrapper

# Load environment variables
load_dotenv()

# Create bot instance with intents
intents = discord.Intents.default()
intents.message_content = True  # Required for message content access

bot = discord.Client(intents=intents)

def trimText(text, max_line=10):
    lines = text.splitlines()
    num_line = min(max_line, len(lines))
    trimmed_text = '\n'.join(lines[:num_line])
    if len(lines) > num_line:
        trimmed_text = trimmed_text + "\n..."
    return trimmed_text

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    
    # Send message to specific channel
    channel_id = int(os.getenv('DISCORD_CHANNEL_ID'))
    channel = bot.get_channel(channel_id)
    
    if channel:
        articles = meethk_scrapper.getMeetHKArticleObjects()
        latest_notice_title = articles[0].title
        notice_content = trimText(articles[0].postContentPureText, 10)
        notice_url = articles[0].postLink
        message = discord.Embed(title=str(latest_notice_title), description=str(notice_content), url=str(notice_url), colour=discord.Color.teal())
        await channel.send(embed=message)
    else:
        print(f"Channel with ID {channel_id} not found")

# Run the bot with your token
bot.run(os.getenv('DISCORD_TOKEN'))