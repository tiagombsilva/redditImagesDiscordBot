import mysql.connector
from config import Config

subreddits = Config.subReddits

class database:
    __host = Config.json["database"]["host"]
    __user = Config.json["database"]["user"]
    __passwd= Config.json["database"]["password"]

    def __init__(self):
        self.db =  mysql.connector.connect(host=self.__host,user=self.__user,passwd=self.__passwd)
        self.cursor = self.db.cursor()
        self.initializeDb()

    def initializeDb(self):
        print("Initializing db")
        for line in open("db/createDB.sql"):
            self.cursor.execute(line)
        print("Creating tables")
        for subreddit in subreddits:
            query = "CREATE TABLE "+subreddit+"(id int primary key auto_increment, url varchar(255))"
            self.cursor.execute(query)
            self.db.commit()

    def getAllHistory(self,tableName):
        self.cursor.execute("SELECT * FROM "+tableName)
        return self.cursor.fetchall()

    def insertImage(self,imageUrl,tableName):
        query = """INSERT INTO """+tableName+""" VALUES (NULL,%s)"""
        record=[(imageUrl)]
        self.cursor.execute(query,record)
        self.db.commit()

    def exists(self,url,subreddit):
        exists = False
        for row in self.getAllHistory(subreddit):
                if(row[1] == url):
                    exists=True
        return exists

        