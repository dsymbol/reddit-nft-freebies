# reddit-nft-freebies

<div align="center">
<img src="https://user-images.githubusercontent.com/88138099/142779007-babd0822-192a-41db-a186-30f0b8f17318.png"/></br>
<i>example of a giveaway being held on the <a href="https://www.reddit.com/r/NFTsMarketplace/">subreddit</a></i>
</div>

## Prerequisites

- [Python](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/get-docker/) (If you intend on deploying the app as a Docker image)

## Install

There are two ways to begin using the bot, depending on your preference:

### Manual

```bash
git clone https://github.com/dsymbol/reddit-nft-freebies
cd reddit-nft-freebies
pip install praw
python main.py
```

### Docker

```bash
git clone https://github.com/dsymbol/reddit-nft-freebies
cd reddit-nft-freebies
docker build -t reddit-nft-freebies .
docker run -d --name reddit-nft-freebies -v `pwd`/config.py:/app/config.py reddit-nft-freebies:latest
```

## Configuration

Before running the bot, you must first set it up so it can connect to the Reddit API. Create a config.py file and fill in the following information:

- `REDDIT_CLIENT_ID`: client id from reddit app
- `REDDIT_CLIENT_SECRET`: client secret from reddit app
- `REDDIT_USERNAME`: account username
- `REDDIT_PASSWORD`: account password
- `ETH_ADDRESS`: your ethereum wallet address
- `SOL_ADDRESS`: your solana wallet address

#### Create a Reddit app

1. Go to your [app preferences](https://old.reddit.com/prefs/apps/), and click on "Create an app" button at the bottom of the page.

2. Fill out the "Create application" form, it doesn't matter what you fill inside it except the "type" section in which you must select "script".

3. Click on the "Create app" button. Your newly created app should now appear under the "Developed applications" section!

4. Copy the **ID** and **SECRET** of your app.
