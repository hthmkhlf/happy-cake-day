import praw
import prawcore
import sqlite3
import time
import logging
from time import  gmtime ,strftime
from datetime import datetime, date


#Reddit stuff
reddit = praw.Reddit("cakeBot", user_agent="Cake bot user agent")
subreddit = reddit.subreddit("all")

#Create the databse connections 
db_conn = sqlite3.connect('cake.db')

#Create Logging file to track the database
logger  = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('learn.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)



#Add the user to the database if they are not on its
def isCake(user:str,submission:str):
    db_cur = db_conn.cursor()
    find_user = "Select userId FROM cake_users where userID=?"
    add_user = "INSERT INTO cake_users(userID,pubID) VALUES(?,?)"
    try:
        db_cur.execute(find_user,(str(user),))
        result = db_cur.fetchone()
        if not result:
            db_cur.execute(add_user,(str(user),str(submission),))
            logger.debug('User was added to the database')
            db_conn.commit()
    except sqlite3.Error as e:
        logger.critical(f"User was:{user}, submission was: {submission}")
        logger.error(e, exc_info=True)
    



def main():
    try:
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
            if (cur_day == user_cake_day) and (cur_month == user_cake_month) and (cur_date.year != user_created.year) and (comment.subreddit.over18 == False):
                isCake(comment.author, comment.id)
                # print(f"Happy cake day 🎂🎂🎂🎂🎂🎂🎂🎂🎂🎂🎂🎂 {comment.author}")
            else:
                # print(f"{comment.author} are not celebrating their Cake Day")
                isCake(str(comment.author), str(comment.id))
    except prawcore.exceptions.NotFound as e:
        logger.error(e, exc_info=True)
        time.sleep(10)
        main()
            


        


if __name__ == "__main__":
    main()
