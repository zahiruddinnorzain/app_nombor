import tweepy

def get_api(cgf):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def main():
    # Fill in the values noted in previous step here
    cfg = {
        "consumer_key"          : "99iFuCOTzNQb5oMpNfT9IVZAN",
        "consumer_secret"       : "Rm7e8jOE06q0jGny3pUDP36Xafxb3njjhZCarb8gDqxd1a5ihb",
        "access_token"          : "906176499320897536-mlic1L6oJAY815owEY5wBdTZ9bOmPpm",
        "access_token_secret"   : "TeqFHKEGSVOxqj5MmFfACVM2ZlfRqq65c7LTiEM873Q2H",
    }

    api = get_api(cfg)
    tweet = "tweet from pyhton_1"
    status = api.update_status(status=tweet)
    # yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
    main()
