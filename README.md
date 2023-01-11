## Reddit NFT Freebies

<img src="https://user-images.githubusercontent.com/88138099/142779007-babd0822-192a-41db-a186-30f0b8f17318.png" alt="Example of a giveaway being held on the subreddit" align="center"/>

<i>Example of a giveaway being held on the <a href="https://www.reddit.com/r/NFTsMarketplace">subreddit</a></i>

## Prerequisites
- [Python](https://www.python.org/downloads)
- [Docker](https://docs.docker.com/get-docker) (If you intend on deploying the app as a Docker image)

## Install

There are two ways to begin using the bot, depending on your preference:

### Manual
```sh
git clone https://github.com/dsymbol/reddit-nft-freebies.git
cd reddit-nft-freebies
pip install -r requirements.txt
python main.py
```

## Docker
```sh
git clone https://github.com/dsymbol/reddit-nft-freebies.git
cd reddit-nft-freebies
docker build -t reddit-nft-freebies .
docker run -d --name reddit-nft-freebies -v `pwd`/config.py:/app/config.py reddit-nft-freebies:latest
```

## Configuration

Before running the bot, you must first set it up so it can connect to the Reddit API. Create a config.py file and fill in the following information:

- `REDDIT_CLIENT_ID`: client id from reddit app
- `REDDIT_CLIENT_SECRET`: client secret from reddit app
- `REDDIT_USERNAME`: reddit account username
- `REDDIT_PASSWORD`: reddit account password
- `ETH_ADDRESS`: your ethereum wallet address

#### Create a Reddit App

1. Go to the [Reddit App preferences](https://old.reddit.com/prefs/apps/) and click on the "Create an app" button at the bottom of the page.

2. Fill out the "Create application" form. The "type" section must be set to "script".

3. Click on the "Create app" button. Your newly created app should now appear under the "Developed applications" section.

4. Copy the **ID** and **SECRET** of your app.
