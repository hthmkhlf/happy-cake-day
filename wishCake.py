import praw
import prawcore
import sqlite3
import logging
from datetime import datetime, date


#Script that will wish the user a happy cake day


#Reddit stuff
reddit = praw.Reddit("cakeBot", user_agent="Cake bot user agent")
subreddit = reddit.subreddit("all")

#Create the databse connections 
db_conn = sqlite3.connect('cake.db')



def get_user_comments(user:str):
    comment_karma = None
    best_comment_id = None
    num = 0
    for submission in reddit.redditor(str(user)).comments.top("year",limit=99999):
        num += 1
    print(num)
    
def get_user_posts(user:str):
    post_karma = None
    best_post_karma = None
    num = 0
    for submission in reddit.redditor(str(user)).submissions.top("year",limit=99999):
        num += 1
    
    print(num)
        


def wish_cake():
    pass


if __name__ == "__main__":
    # get_user_posts("AutoModerator")
    get_user_comments("AutoModerator")