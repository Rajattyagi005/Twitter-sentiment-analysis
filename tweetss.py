import tweepy
from tweepy import OAuthHandler

api_key='NvzXMjQNuarSAmQyGmhmRNYfj'
api_secret='TJw0mthNx7PjVQ4QHNTIPWtLY2aoFUvRHoQlcKRGkHbAEiTD1j'
access_token='931780055914618880-H7MqFndJV2uSDXGtxhNzF5ubYyIffXW'
access_token_secret='3B6n5QU36oQNJUKpSj7nlSMsOqWl3uoaZERiJtipzi2Kr'

 
auth = OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)    
    
from tweepy import Stream
from tweepy.streaming import StreamListener
 
class MyListener(StreamListener):    
 
    def on_data(self, data):                      
        try:
            with open('output.json', 'a') as f:  
                f.write(data)
                print(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())

#change the keyword here
twitter_stream.filter(track=['Congress'])





