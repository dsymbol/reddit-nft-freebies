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
    account = api(reddit_client_id, reddit_client_secret, reddit_username, reddit_password)
    reddit = account.authorize()
    reddit.read_only = False
    subreddit = reddit.subreddit("NFTsMarketplace")
    replied_to = load_db("commentdb.txt")
    keywords = ["wallet", "address"]

    while True:
        print("[!] Starting bot...")
        for post in subreddit.hot(limit=25):
            if post not in replied_to and any(x in post.title.lower() for x in keywords):
                replied_to.append(post)
                with open('commentdb.txt', 'a') as f:
                    f.write(str(post) + "\n")
                if "sol" in post.title.lower():
                    post.reply(soladdress)
                else:
                    post.reply(ethaddress)
                post.upvote()
                print(f'[+] {post.title}')
                random_sleep = random.randint(300, 600)
                to_mins = random_sleep / 60; to_mins = round(to_mins, 1)
                print(f"[!] Sleeping for {str(to_mins)} minutes") 
                sleep(random_sleep)        
        print("[*] Commented on all posts matching keywords, sleeping for six hours.\n")
        sleep(21600)       

if __name__ == '__main__':
    main()