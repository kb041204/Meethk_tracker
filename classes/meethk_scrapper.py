import requests
from bs4 import BeautifulSoup
import traceback

from .MeetHKArticle import MeetHKArticle

MEETHK_URL = "https://www.meethk.com/"

def getSoup(url):
    try:
        res = requests.get(url)
        return BeautifulSoup(res.text, 'html.parser')
    except Exception as e: #AVA Server error
        tb = traceback.format_exc()
        print("Exception in getSoup, url: " + str(url) + ", traceback:")
        print(str(tb))

def getAllArticles(soup):
    return soup.find_all("article")

def getMeetHKArticleObjects():
    soup = getSoup(MEETHK_URL)
    raw_articles = getAllArticles(soup)
    articles = []
    
    for (idx, raw_article) in enumerate(raw_articles):
        meetHKArticle = MeetHKArticle(raw_article)
        print("idx[" + str(idx) + "], post_id=" + str(meetHKArticle.postId) + ", timestamp=" + str(meetHKArticle.postDateTime))
        articles.append(meetHKArticle)
    return articles