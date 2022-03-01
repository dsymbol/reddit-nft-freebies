from prawcore import ResponseException
from datetime import datetime
from time import sleep
from config import *
import random
import praw
import string
import sys
import os

class api:
    def __init__(self, client_id, client_secret, username, password):
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self.user_agent = api.uagent(10)

    @staticmethod
    def uagent(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    def authorize(self):
        return praw.Reddit(
            client_id = self.client_id,
            client_secret = self.client_secret,
            user_agent = self.user_agent,
            username = self.username,
            password = self.password,
            )
    
    def authorized(self, reddit):
        try:
            reddit.user.me()
        except ResponseException:
            print("Invalid credentials")
            sys.exit()
        else:
            print(f"Logged in as: {self.username}")
            width = 13 + len(self.username)
            print('-' * width)
            sleep(1)

def load_file(file):
    try:
        l = []
        with open(file, 'r') as f:
            for line in f:
                l.append(line.rstrip())
        return l
    except FileNotFoundError:
        with open('comment.db', 'w') as f:
            pass
        return []

def get_nft():
    account = api(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD)
    reddit = account.authorize()
    account.authorized(reddit)
    reddit.read_only = False
    commented = load_file("comment.db")
    subreddit = reddit.subreddit("NFTsMarketplace")
    keywords = ["wallet", "address"]
    sleep(1)
    
    while True:
        try:
            for post in subreddit.hot(limit=25):
                if (post not in commented and any(x in post.title.lower() for x in keywords) 
                        or post not in commented and keywords[1] in post.link_flair_text):
                    commented.append(post)
                    with open('comment.db', 'a') as f:
                        f.write(f"{str(post)}\n")
                    post.reply(ETH_ADDRESS)
                    post.upvote()
                    print(f'{post.title}')
                    rndm_sleep = random.randint(300, 600); to_mins = rndm_sleep / 60; to_mins = round(to_mins, 1)
                    print(f"zZz for {str(to_mins)} minutes")
                    sleep(rndm_sleep)
        except:
            print("Error occured, retrying.")
            sleep(500)
        print("+")
        print(f"[{datetime.now().replace(microsecond=0)}] zZz for 6 hours")
        sleep(21600)

def main():
    get_nft()

if __name__ == '__main__':
    main()
