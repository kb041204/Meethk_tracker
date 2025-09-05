import requests
from bs4 import BeautifulSoup
import traceback
from datetime import datetime

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

def getTitleFromArticle(article):
    h2_element = article.find("h2", class_="post-title")
    a_element = h2_element.find("a")
    return a_element.text

def getPostDateFromArticle(article):
    p_element = article.find("p", class_="post-date")
    time_element = p_element.find("time")
    return datetime.strptime(time_element["datetime"], "%Y-%m-%d %H:%M:%S")

def main():
    soup = getSoup(MEETHK_URL)
    articles = getAllArticles(soup)
    for article in articles:
        title = getTitleFromArticle(article)
        print("title: " + str(title))
        post_datetime = getPostDateFromArticle(article)
        print("post datetime: " + str(post_datetime))
    
main()