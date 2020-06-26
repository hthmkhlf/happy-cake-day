import praw
import sqlite3


reddit = praw.Reddit("cakeBot", user_agent="Cake bot user agent")
subreddit = reddit.subreddit("all")

