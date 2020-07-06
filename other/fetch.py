import requests
import praw 
import prawcore
from datetime import datetime
import time


url = "https://api.pushshift.io/reddit/{}/search?limit=1000&sort=desc&author={}&after={}"
one_year_ago = 315_569_26.00
current_time = time.mktime(time.localtime())

def get_user_data(username:str, object_type:str):
    start_time = current_time - one_year_ago
    print(time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(start_time)))
    new_url = f"https://api.pushshift.io/reddit/{object_type}/search?limit=1000&sort=desc&author={username}&after={start_time}"



get_user_data("Atara117","comment")