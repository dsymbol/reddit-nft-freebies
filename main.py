from datetime import datetime
from utils.api import API
from time import sleep
from config import *
import random

def load_file(file):
    """
    Loads the specified file and returns its contents as a list of strings,
    where each string represents a line in the file.
    If the file is not found, it creates an empty file called 'comments.db'
    and return an empty list.

    :param file: The file to load
    :type file: str
    :return: The contents of the file as a list of strings
    :rtype: list
    """
    try:
        with open(file, 'r') as f:
            return [line.rstrip() for line in f]
    except FileNotFoundError:
        with open('comments.db', 'w') as f:
            pass
        return []

# Function to get NFTs
def get_nft():
    """
    This function gets NFTs from the subreddit 'NFTsMarketplace' using the Reddit API.
    It replies to the post with the Ethereum wallet address and upvotes the post.
    It also keeps a log of the posts that it has already commented on, in a file named 'comment.db'
    """
    # Authorize and get the subreddit
    account = API(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD).authorize()
    commented = load_file("comment.db")
    subreddit = account.subreddit("NFTsMarketplace")

    # keywords to look for in post titles
    keywords = ["wallet", "address"]
    sleep(1)

    while True:
        try:
            # Get the hot posts from the subreddit
            for post in subreddit.hot(limit=25):
                # Check if post is not commented and has keywords in title or post flair text
                if (post not in commented and any(x in post.title.lower() for x in keywords)
                        or post not in commented and keywords[1] in post.link_flair_text):
                    commented.append(post)
                    # Write the post to comment.db
                    with open('comments.db', 'a') as f:
                        f.write(f"{str(post)}\n")
                    # Reply to the post with ETH_ADDRESS and upvote
                    post.reply(body=ETH_ADDRESS)
                    post.upvote()
                    print(f'{post.title}')
                    # Sleep for a random duration before commenting on next post
                    rndm_sleep = random.randint(300, 600);
                    to_mins = rndm_sleep / 60;
                    to_mins = round(to_mins, 1)
                    print(f"zZz for {str(to_mins)} minutes")
                    sleep(rndm_sleep)
        except:
            print("Error occurred, retrying.")
            sleep(500)
        print("+")
        print(f"[{datetime.now().replace(microsecond=0)}] zZz for 6 hours")
        # Sleep for 6 hours
        sleep(21600)


if __name__ == '__main__':
    get_nft()
