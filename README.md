# reddit-nft-freebies

Comments on hot [/r/NFTsMarketplace](https://www.reddit.com/r/NFTsMarketplace/) airdrop posts with your wallet address.

## Install
There are two ways to begin using the bot, depending on your preference:

### Manual

Make sure [Python](https://www.python.org/downloads/) is installed on your system and open a terminal.

```bash
git clone https://github.com/dsymbol/reddit-nft-freebies
cd reddit-nft-freebies
pip install praw
python main.py
```

### Docker CLI

Build the image using the `Dockerfile`:

```
docker build -t reddit-nft-freebies .
```

Run the image:

```
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
