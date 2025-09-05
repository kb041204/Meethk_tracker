import requests
from bs4 import BeautifulSoup
import traceback

from classes.MeetHKArticle import MeetHKArticle

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

def main():
    soup = getSoup(MEETHK_URL)
    articles = getAllArticles(soup)
    for article in articles:
        meetHKArticle = MeetHKArticle(article)
        print("title: " + str(meetHKArticle.title))
        print("post_id: " + str(meetHKArticle.postId))
        print("post datetime: " + str(meetHKArticle.postDateTime))
        print("categories: " + str(meetHKArticle.categories))
        print("link: " + str(meetHKArticle.postLink))
        print("pure_text: " + str(meetHKArticle.postContentPureText))
        break
main()