import praw
import sqlite3
import logging
from time import  gmtime ,strftime
from datetime import datetime, date


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
        # if comment.subreddit.over18 == False:
        #Date variables
        cur_date = date.today()
        cur_day = cur_date.day
        cur_month = cur_date.month
        user_created = datetime.fromtimestamp(comment.author.created_utc).date()
        user_cake_day = user_created.day
        user_cake_month = user_created.month
        # Check if the user is on cake day
        if (cur_day == user_cake_day) and (cur_month == user_cake_month) and (cur_date.year != user_created.year) :
            print(f"Happy cake day {comment.author}")
        else:
            print(f"No cake today: {cur_day} : {user_cake_day} -- {cur_month} : {user_cake_month} -- {cur_date.year} : {user_created.year}")
        


if __name__ == "__main__":
    main()
