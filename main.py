from time import sleep
from config import *
import praw
import string
import random

class api:
    def __init__(self, client_id, client_secret, username, password):
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self.user_agent = random_string(10)

    def authorize(self):
        return praw.Reddit(
                        client_id = self.client_id,
                        client_secret = self.client_secret,
                        user_agent = self.user_agent,
                        username = self.username,
                        password = self.password,
                        )

def random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def load_db(file):
    list = []
    with open(file, 'r') as f:
        for line in f:
            list.append(line.rstrip())
    return list

def main():
    account = api(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD)
    reddit = account.authorize()
    reddit.read_only = False
    subreddit = reddit.subreddit("NFTsMarketplace")
    commented = load_db("commentdb.txt")
    keywords = ["wallet", "address"]

    print(f"Logged in as {REDDIT_USERNAME}")
    sleep(1)
    print("[!] Starting bot...")
    while True:
        print("-")
        for post in subreddit.hot(limit=25):
            if post not in commented and any(x in post.title.lower() for x in keywords) or post not in commented and keywords[1] in post.link_flair_text:
                commented.append(post)
                with open('commentdb.txt', 'a') as f:
                    f.write(f"{str(post)}\n")
                if "sol" in post.title.lower():
                    post.reply(SOL_ADDRESS)
                else:
                    post.reply(ETH_ADDRESS)
                post.upvote()
                print(f'[+] {post.title}')
                random_sleep = random.randint(300, 600)
                to_mins = random_sleep / 60; to_mins = round(to_mins, 1)
                print(f"[-] Sleeping for {str(to_mins)} minutes") 
                sleep(random_sleep)        
        print("[*] Commented on all hot posts matching keywords, sleeping for six hours.")
        sleep(21600)       

if __name__ == '__main__':
    main()
