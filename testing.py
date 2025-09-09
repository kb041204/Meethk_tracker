from classes import meethk_scrapper

def getRawArticles():
    soup = meethk_scrapper.getSoup(meethk_scrapper.MEETHK_URL)
    return meethk_scrapper.getAllArticles(soup)

def saveLatestArticleSoup():
    raw_articles = getRawArticles()

    for raw_article in raw_articles:
        with open("latest_article.txt", "w", encoding='utf-8') as file:
            file.write(str(raw_article))
            break

def saveAllPageOneArticlesSoup():
    raw_articles = getRawArticles()

    for (idx,raw_article) in enumerate(raw_articles):
        with open("article" + str(idx) + ".txt", "w", encoding='utf-8') as file:
            file.write(str(raw_article))

meethk_scrapper.getMeetHKArticleObjects()