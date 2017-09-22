import tweepy
import os
import sys

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def main():
    os.system('cls')
    now_status = "Welcome\nType 'quit' to exit"
    while 1:

        print ('================')
        print ('Status:\n')
        print (now_status)    # show status here
        print ('\n================')
        print ('\n')

        twit = raw_input('Giliran: ')   #input nombor giliran

        if twit == 'quit' or twit == 'QUIT' or twit == 'exit' or twit == 'EXIT' or twit == "'quit'" :     # exit console
            os.system('cls')
            sys.exit()
            break

        try:    # try to post
            # Fill in the values noted in previous step here
            cfg = {
                "consumer_key"          : "99iFuCOTzNQb5oMpNfT9IVZAN",
                "consumer_secret"       : "Rm7e8jOE06q0jGny3pUDP36Xafxb3njjhZCarb8gDqxd1a5ihb",
                "access_token"          : "906176499320897536-mlic1L6oJAY815owEY5wBdTZ9bOmPpm",
                "access_token_secret"   : "TeqFHKEGSVOxqj5MmFfACVM2ZlfRqq65c7LTiEM873Q2H",
                }

            api = get_api(cfg)
            tweet = twit    #string to tweet number
            status = api.update_status(status=tweet)
            # yes, tweet is called 'status' rather confusing

            now_status = ("OK " + twit)  # status for success post

        except Exception as e:   # Fail to post
            now_status = e
            #now_status = ("ERROR " + e + "at post " + twit)

        os.system('cls')    # clear screen for windows shell




if __name__ == "__main__":
    main()
