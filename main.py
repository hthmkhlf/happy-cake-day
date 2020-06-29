import praw
import sqlite3
from time import  gmtime ,strftime


#Reddit stuff
reddit = praw.Reddit("cakeBot", user_agent="Cake bot user agent")
subreddit = reddit.subreddit("all")

#Create the databse connections 
db_conn = sqlite3.connect('cake.db')

#Function called if the user is on his cake day it will add them to the database in order for the wishCake script to send them a happy cake day message
def isCake(user:str,submission:str):
    db_cur = db_conn.cursor()
    find_user = "Select userId FROM cake_users where userID=?"
    add_user = "INSERT INTO cake_users(userID,pubID) VALUES(?,?)"
    db_cur.execute(find_user,(user,))
    result = db_cur.fetchone()
    if result:
        print("User in database")
    else:
        print("Not found")


def main():
    pass


if __name__ == "__main__":
    # main()
    isCake('abc','abc')
