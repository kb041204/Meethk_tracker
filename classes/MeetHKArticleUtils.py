from datetime import datetime

def getTitleFromArticle(article):
    h2_element = article.find("h2", class_="post-title")
    a_element = h2_element.find("a")
    return a_element.text

def getPostDateFromArticle(article):
    p_element = article.find("p", class_="post-date")
    time_element = p_element.find("time")
    return datetime.strptime(time_element["datetime"], "%Y-%m-%d %H:%M:%S")

def getPostCategories(article):
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

def getPostId(article):
    return article["id"]