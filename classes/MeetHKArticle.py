from . import MeetHKArticleUtils as meetHKArticleUtils

class MeetHKArticle():
    def __init__(self, article):
        self.title = meetHKArticleUtils.getTitleFromArticle(article)
        self.postDateTime = meetHKArticleUtils.getPostDateFromArticle(article)
        self.categories = meetHKArticleUtils.getPostCategories(article)
        self.postLink = meetHKArticleUtils.getPostLink(article)
        self.postContentPureText = meetHKArticleUtils.getPostContentPureText(article)
        self.postId = meetHKArticleUtils.getPostId(article)