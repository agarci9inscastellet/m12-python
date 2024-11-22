import os
import time

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener


# this will print out the subscription status to console
class Listener(SubscribeListener):
    def status(self, pubnub, status):
        print(f'Status: \n{status.category.name}')


# here we create configuration for our pubnub instance
config = PNConfiguration()
config.subscribe_key = 'sub-c-57344397-071a-462c-8c4d-c6be305a4e84'
config.publish_key = 'pub-c-53eb2993-fb8c-48d4-b96c-3eaaaa1af0f7'
config.user_id = 'example2'
config.enable_subscribe = True
config.daemon = True

pubnub = PubNub(config)
pubnub.add_listener(Listener())

subscription = pubnub.channel('example').subscription()
subscription.on_message = lambda message: print(f'Message from {message.publisher}: {message.message}')
subscription.subscribe()

count=0
while True:
    count +=1
    msg=input();
    publish_result = pubnub.publish().channel("example").message(config.user_id+":"+msg).sync()

pubnub.stop()
time.sleep(1)
print('Bye.')