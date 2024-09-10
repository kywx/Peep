# Peep
Peep posts a cat image on twitter. That's it.

## Installation
First, install tweepy using the package manager pip to get easy access the twitter api endpoints.

It's not necessary, but you can also install python-dotenv to keep your tokens handy in a .env file and away from the actual python file. Just replace the variables in the .py file if you don't care for it.

```bash
pip install tweepy
python.exe -m pip install --upgrade pip
pip install python-dotenv
```

## Usage
Just put in your api tokens and click run. (Scroll down if you don't have the api tokens)

It's a good skeleton to edit. The only important parts are authen_v1 and authen_v2.

## Nice to know
This utilizes only the free tier of the api access stuff. All this version is good for is posting and deleting tweets. You can also get some information about yourself and other users.

You are allowed very limited endpoints from both v1 and v2 of the api.

## Developer's Account and API Tokens
As of 9/10/24, the official tutorial from x: [https://developer.x.com/en/docs/x-api/getting-started/getting-access-to-the-x-api](https://developer.x.com/en/docs/x-api/getting-started/getting-access-to-the-x-api)

Click sign up. Then sign up. Then apply for an app.

Then go into the app's settings and look for User authentication settings.

Make sure to give it read and write permissions. For the app info section, if you don't care, then you can just put any url for callback and website. I used https:// x.com. Click save.

Now, go into the app's keys and tokens. Regenerate them, even if you already did that. Under Authentication Tokens, it should say "Created with Read and Write permissions" or something like that.

If you didn't save them, regenerate them and save them.
