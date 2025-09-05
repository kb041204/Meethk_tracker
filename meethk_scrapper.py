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

def getPostCategory(article):
    categories = []
    for tag in article["class"]:
        if tag.startswith("category-"):
            categories.append(tag)
    return categories

def getPostLink(article):
    h2_element = article.find("h2", class_="post-title")
    a_element = h2_element.find("a")
    return a_element["href"]

def getPostContentPureText(article):
    div_element = article.find("div", class_="entry")
    return div_element.get_text().strip()

def getPostID(article):
    return article["id"]

def main():
    soup = getSoup(MEETHK_URL)
    articles = getAllArticles(soup)
    for article in articles:
        title = getTitleFromArticle(article)
        print("title: " + str(title))
        post_id = getPostID(article)
        print("post_id: " + str(post_id))
        post_datetime = getPostDateFromArticle(article)
        print("post datetime: " + str(post_datetime))
        categories = getPostCategory(article)
        print("categories: " + str(categories))
        link = getPostLink(article)
        print("link: " + str(link))
        pure_text = getPostContentPureText(article)
        print("pure_text: " + str(pure_text))
        break
main()