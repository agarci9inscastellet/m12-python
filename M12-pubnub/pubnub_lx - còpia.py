import os
import time

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener

# this will print out the subscription status to console
class Listener(SubscribeListener):
    def __init__(self, message_handler):
        super().__init__()
        self.message_handler = message_handler

    def status(self, pubnub, status):
        print(f'Status: \n{status.category.name}')
    
    def message(self, pubnub, message):
        if (message.publisher != pubnub.config.user_id):
            self.message_handler(message.publisher, message.message)
        


# here we create configuration for our pubnub instance

def pubnub_init(userid, chanel, listener):
    config = PNConfiguration()
    ### cal agafar aquests tokens de la web pubnub, on diu Demo Keyset
    config.subscribe_key = 'sub-c-57344397-071a-462c-8c4d-c6be305a4e84'
    config.publish_key = 'pub-c-53eb2993-fb8c-48d4-b96c-3eaaaa1af0f7'
    #aquest és el nom de l'usuari que faci login
    config.user_id = userid
    config.enable_subscribe = True
    config.daemon = True

    pubnub = PubNub(config)
    pubnub.add_listener(Listener(listener))

    subscription = pubnub.channel(chanel).subscription()
    #subscription.on_message = lambda message: print(f'\n<<< From {message.publisher}: {message.message}\n>>>',end="") if message.publisher != config.user_id else time.sleep(0.5)  
    subscription.subscribe()
    time.sleep(0.5)
    subscribed_channels = pubnub.get_subscribed_channels()
    print("Subscribed channels:", subscribed_channels[0])
    return pubnub
   
def pubnub_send(pubnub, msg):
    subscribed_channels = pubnub.get_subscribed_channels()
    publish_result = pubnub.publish().channel( subscribed_channels[0]).message(msg).sync() 
    return publish_result