# pip install tweepy
# python.exe -m pip install --upgrade pip
# pip install python-dotenv

import requests
import tweepy
import os
from dotenv import load_dotenv, set_key, find_dotenv
from time import sleep

# requires a .env file in the root directory
dotenv_file = find_dotenv()
load_dotenv()
bearer_token = os.getenv("bearer_token")
api_key = os.getenv("api_key")
api_secret = os.getenv("api_secret")
access_key = os.getenv("access_key")
access_secret = os.getenv("access_secret")


def random_cat_url():
    res = requests.get("https://api.thecatapi.com/v1/images/search").json()
    return res[0]["url"]


def downloaded_img(url, filename):
    r = requests.get(url)
    with open(filename, 'wb') as outfile:
        outfile.write(r.content)


def delete_img(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("file does not exist")
    pass


def authen_v2():
    # twitter api version 2
    client = tweepy.Client(consumer_key=api_key, consumer_secret=api_secret,
                           access_token=access_key, access_token_secret=access_secret)
    return client


def authen_v1():
    # twitter api version 1
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_key, access_secret)
    
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication Successful")
    except:
        print("Authentication Error")
    return api


def random_fact():
    # gets from a free online api
    req = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random").json()
    return req['text']


def random_dadjoke():
    # gets froms a free online api
    headers = {"Accept": "application/json"}
    req = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return req['joke']


def reply(client, twt_id, text=""):
    # still working on getting the tweet id of a mention
    client.create_tweet(text=text, in_reply_to_tweet_id=twt_id)


def main():
    # uses twitter api v1 to upload media and twitter api v2 to post
    url = random_cat_url()
    filepath = "img/" + url.rsplit('/', 1)[-1]
    downloaded_img(url, filepath)
    api = authen_v1()
    media = api.media_upload(filepath)
    
    client = authen_v2()
    # posts tweet with #1..2..3..4
    client.create_tweet(text=f'#{os.getenv("num")}', user_auth=True, media_ids=[media.media_id])
    # posts a tweet with a random dad joke
    # client.create_tweet(text=random_dadjoke(), user_auth=True, media_ids=[media.media_id])
    set_key(dotenv_file, "num", str(int(os.getenv("num"))+1))
    print("Posted")
    delete_img(filepath)    # delete or comment this line to store photos in img/ folder


if __name__ == "__main__":
    main()  # posts once

    """
    uncomment to post every hour

    while True:
        main()
        sleep(3600)
        # waits 3600 seconds(1 hour) until posting again
    """
