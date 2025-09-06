import discord
from discord.ext import tasks
import os
from dotenv import load_dotenv
from classes import meethk_scrapper
import datetime

# Load environment variables
load_dotenv()

# Create bot instance with intents
intents = discord.Intents.default()
intents.message_content = True  # Required for message content access

bot = discord.Client(intents=intents)

articles_saved = []

def trimText(text, max_line=10):
    lines = text.splitlines()
    num_line = min(max_line, len(lines))
    trimmed_text = '\n'.join(lines[:num_line])
    if len(lines) > num_line:
        trimmed_text = trimmed_text + "\n..."
    return trimmed_text

def createDiscordEmbedMessage(article):
    latest_notice_title = article.title
    notice_content = trimText(article.postContentPureText, 10)
    notice_url = article.postLink
    return discord.Embed(title=str(latest_notice_title), description=str(notice_content), url=str(notice_url), colour=discord.Color.teal())

@bot.event
async def on_ready():
    global articles_saved
    print(f'{bot.user} has connected to Discord!')
    articles_saved = meethk_scrapper.getMeetHKArticleObjects()
    checkMeetHK.start()

@tasks.loop(minutes=10.0)
async def checkMeetHK():
    print(f'{str(datetime.datetime.now())} Check MeetHK starts')
    global articles_saved
    articles_retrieved = meethk_scrapper.getMeetHKArticleObjects()
    for article_retrieved in articles_retrieved:
        matching_article_found = False
        for article_saved in articles_saved:
            if article_retrieved.postId == article_saved.postId:
                matching_article_found = True
                break
        
        if not matching_article_found:
            # article not saved
            message = createDiscordEmbedMessage(article_retrieved)
            
            # Send message to specific channel
            channel_id = int(os.getenv('DISCORD_CHANNEL_ID'))
            channel = bot.get_channel(channel_id)
            if channel:
                print(f"=========Sending message to channel")
                await channel.send(embed=message)
            else:
                print(f"Channel with ID {channel_id} not found")
            
    articles_saved = articles_retrieved
    print(f'{str(datetime.datetime.now())} Check MeetHK ends')

# Run the bot with your token
bot.run(os.getenv('DISCORD_TOKEN'))