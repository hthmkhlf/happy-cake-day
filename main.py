import praw
import sqlite3
import logging
from time import  gmtime ,strftime


#Reddit stuff
reddit = praw.Reddit("cakeBot", user_agent="Cake bot user agent")
subreddit = reddit.subreddit("all")

#Create the databse connections 
db_conn = sqlite3.connect('cake.db')

#Create Logging file to track the database
logging.basicConfig(filename='dberr.log',level=logging.DEBUG)

#Add the user to the database if they are not on its
def isCake(user:str,submission:str):
    db_cur = db_conn.cursor()
    find_user = "Select userId FROM cake_users where userID=?"
    add_user = "INSERT INTO cake_users(userID,pubID) VALUES(?,?)"
    try:
        db_cur.execute(find_user,(user,))
        result = db_cur.fetchone()
        if not result:
            db_cur.execute(add_user,(user,submission,))
            db_conn.commit()
            db_conn.close()
    except sqlite3.Error as e:
        logging.exception("Error occured on the isCake function", exc_info=True)
    



def main():
    for comment in subreddit.stream.comments():
        if 
        print(comment.subreddit )


if __name__ == "__main__":
    main()
    # pass
