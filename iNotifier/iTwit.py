# This is notifier
# This is notifier by using twitter

from tweepy import *

class iTwit :
    def __init__(self, user) :
        # consumer login
        self.consumer_key = "iJtae8bcIzlbaapPp0bob0Kzy"
        self.consumer_secret = "gUdJiyNSSKGpYuWNv1oT9Jqe9b9f99ZwCXE5qPm2cuqs99BlvN"

        # consumer login
        self.consumer_key = "iJtae8bcIzlbaapPp0bob0Kzy"
        self.consumer_secret = "gUdJiyNSSKGpYuWNv1oT9Jqe9b9f99ZwCXE5qPm2cuqs99BlvN"

        # access_token login
        self.ACCESS_KEY = "177153021-FyGAaxONJtVfzVDxJBMOu6cEM0NyovcmlMFhGXGK"
        self.ACCESS_SECRET = "IaMxGIikwfP43NJvk1TXOYCckOqCkEZ0Qb0egJW3efIvl"
 
    # send test-DM
    def sendDM(self, msg) :
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.ACCESS_KEY, self.ACCESS_SECRET)
        api = API(auth)
        api.send_direct_message(user='doradoli', text=msg)

'''
def test() :
    try :
        itwit = iTwit('doradoli')
        itwit.sendDM('hello twitter')
    except TweepError as e :
        print "Exception : %s" % e.args[0]
        
test()    
'''
