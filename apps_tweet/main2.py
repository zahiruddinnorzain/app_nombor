import tweepy

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def main():
    while 1:
        twit = raw_input('Giliran: ')
        # Fill in the values noted in previous step here
        cfg = {
            "consumer_key"          : "",
            "consumer_secret"       : "",
            "access_token"          : "",
            "access_token_secret"   : "",
            }

        api = get_api(cfg)
        tweet = twit
        status = api.update_status(status=tweet)
        # yes, tweet is called 'status' rather confusing
        print ("OK " + twit)

        if twit == 'quit' : break


if __name__ == "__main__":
    main()
