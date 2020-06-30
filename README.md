# happy-cake-day 🍰🎂🧁
Bot that wishes Reddit users "Happy Cake Day"

## Concept 

Using praw's streams functionality to get comments in real time from r/all using ```subreddit.stream.comments():``` will solve us the problem of dealing with a while loop.
    
> The main.py file will take care of :
* checking if the user is celebrating their cake day (using ```created_utc``` we can determine if the user is celebrating their cake day Note: epoch time is used)        
* Make sure the user's comment is not on an Adult sub as we don't want our bot to have activity on adult subs.
* Add the user to the cake database and add the comment as well as we will use that later to reply back to the user.

> The wishCake.py will take care of :
* Getting the total comment/posts Karma points the user earned in the past year.
* Highlight their most upvoted comment/post.
* reply back with the data gathered and wish them happy cake day.
* The 'wished' column on the db will be set to 1 so we make sure we only wish happy cake day once to avoid spamming the user.


> Cleaning script will take care of:
* Flushing the database, flushing here means removing all the user which their cake day is done once the time_added in the DB is > 24
## Todo

- [ ] Track user comments and posts in the past year
- [ ] Check if the user is on cake day
- [ ] Dropping the users that we already wished Happy cake day
- [ ] Handle Sqlite errors and make sure the database does not get locked 
- [ ] Handle Praw errors and HTTP 403 errors


## Keep an eye on
  * Excluse adult subs
      * Exclude NSFW posts if they are the top link 


## Track top comments and top post 
  * Simply create two new lists one for a comment and one for a post as we are only tracking comments on SFW subs we will simply check if the comment/post we are at has a higher score if so we replace it and move on.  

## Forking and contribution 🎳
Feel free to contribute as much as you want. If you plan on forking this project remember to create a new [praw.ini file](https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html?highlight=praw.ini)