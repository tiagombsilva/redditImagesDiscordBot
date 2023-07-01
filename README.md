# Simple Reddit Image Retriever Discord bot

Simple bot made with Python & MariaDB

## Requirements

* MariaDB
* Python 3

## Installation

* Download Zip file or checkout the project
* In file config.json
* Setup Discord API Authentication 
* Setup Database Authentication 
* Setup Reddit API Authentication(https://www.reddit.com/prefs/apps/)

* Edit subReddits section with the ones you want.

* Run the Bot! 

```bash
python src/index.py
```

## Usage

The Bot will search for all the tags "a", in the the selected subreddits, inserting the link in the database to not repeat the same image twice and finally sends it to the discord channel.
(The channel must be NSFW)

## Tech

Python, PRAW (Reddit API Wrapper), discordpy (Discord API Wrapper), MechanicalSoup and MariaDB
