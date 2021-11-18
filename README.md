# reddit-nft-freebies

<div align="center">
<img src="https://user-images.githubusercontent.com/88138099/142375829-577ddfc6-9a8a-4a08-94f2-745babbe858b.png"/></br>
<i>example of a giveaway being held on the <a href="https://www.reddit.com/r/NFTsMarketplace/">subreddit</a></i>
</div>

## Description
The bot automatically comments on hot [/r/NFTsMarketplace](https://www.reddit.com/r/NFTsMarketplace/) airdrop posts with your wallet address in an attempt to claim freebie NFTs.

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

```
git clone https://github.com/dsymbol/reddit-nft-freebies
cd reddit-nft-freebies
docker build -t reddit-nft-freebies .
docker run -d --name reddit-nft-freebies -v `pwd`/config.py:/app/config.py reddit-nft-freebies:latest
```

## Configuration

Edit `config.py` accordingly:

| Variable                       | Description                      |
| ------------------------------ | ---------------------------------|
| reddit_client_id               | client id from reddit app        |
| reddit_client_secret           | client secret from reddit app    |
| reddit_username                | account username                 |
| reddit_password                | account password                 |
| soladdress                     | your solana wallet address       |
| ethaddress                     | your ethereum wallet address     |

#### Create a Reddit app

1. Go to your [app preferences](https://old.reddit.com/prefs/apps/), and click on "Create an app" button at the bottom of the page.

2. Fill out the "Create application" form, it doesn't matter what you fill inside it except the "type" section in which you must select "script".

3. Click on the "Create app" button. Your newly created app should now appear under the "Developed applications" section!

4. Copy the **ID** and **SECRET** of your app.
