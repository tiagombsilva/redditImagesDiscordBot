from db import database
from config import Config
import praw

redditAuth = Config.json["redditAuth"]
class Website:

    __headers={'user-agent':'Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}

    def __init__(self,site):
        self.site = site
        self.browser = mechanicalsoup.Browser()

    def getAllImages(self):
        entry_page = self.browser.get(self.site,headers=self.__headers)
        tags = entry_page.soup.find_all("a",string="Yes")
        print(tags)

class RedditBot:

    def __init__(self):
        self.reddit = praw.Reddit(client_id=redditAuth["client_id"],
                                  client_secret=redditAuth["client_secret"],
                                  password=redditAuth["password"],
                                  user_agent=redditAuth["user_agent"],
                                  username=redditAuth["username"])
    
    def getSubReddit(self,subreddit):
        return self.reddit.subreddit(subreddit)

    def getListImage(self,subreddit,limitOfFiles):
        imageList=[]
        for submission in subreddit.hot(limit=limitOfFiles):
            imageList.append(submission.url)
        return imageList