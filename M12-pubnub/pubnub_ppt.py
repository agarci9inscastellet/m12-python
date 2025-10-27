import os
import random
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
class Pubnub_lx:
    torn=0
    mytorn=0
    tim=random.randint(0,99)
    ready=False
    jugada=False
    contrincant_id=False

    def __init__(self, userid, chanel):
        config = PNConfiguration()
        ### cal agafar aquests tokens de la web pubnub, on diu Demo Keyset
        config.subscribe_key = 'sub-c-57344397-071a-462c-8c4d-c6be305a4e84'
        config.publish_key = 'pub-c-53eb2993-fb8c-48d4-b96c-3eaaaa1af0f7'
        #aquest és el nom de l'usuari que faci login
        config.user_id = userid
        config.enable_subscribe = True
        config.daemon = True

        pubnub = PubNub(config)

        subscription = pubnub.channel(chanel).subscription()
        subscription.on_message = self.receiver
        time.sleep(0.5)
        subscription.subscribe()
        subscribed_channels = pubnub.get_subscribed_channels()
        print("Subscribed channels:", subscribed_channels[0])
        self.pubnub = pubnub

        while not self.ready:
            self.send( f"wait:{self.tim}") 
            print (f"wait ... {self.ready} - {self.tim} >>> Esperant connexió")
            time.sleep(0.5)
            
        #self.send( f"ready:{self.tim}") 
        #pubnub.add_listener(Listener(listener))

    def receiver(self, message):
        #print("REBUT", message.publisher, message.message)

        if (message.publisher == self.pubnub.config.user_id):
            return
                

        self.contrincant_id=message.publisher
        
        code = message.message[0:4]
      
        if code in ["read","wait"]:
           # if not self.ready:
            #print (f"{code} ... {self.ready} - {self.tim} >>> Connetats amb {message.publisher}")
            self.ready=int(message.message.split(":")[1])
            self.mytorn = self.tim > self.ready 

            if code=="wait":
                self.send( f"ready:{self.tim}") 

        else:
            self.jugada=message.message
            self.torn = not self.torn
            #print("TOOORN ",self.torn)

                
    def play_opponent(self,msg=""):
        if self.torn != self.mytorn:
            if not msg:
                msg=f"Esperant jugada de {self.contrincant_id}"
            print(msg)
            while self.torn != self.mytorn:
                time.sleep(0.2)
            return self.jugada
        return False
  
    def send(self, msg):

        subscribed_channels = self.pubnub.get_subscribed_channels()
        publish_result = self.pubnub.publish().channel( subscribed_channels[0]).message(msg).sync() 
        #print (f"SEND {msg} {subscribed_channels[0]}... {self.ready} - {self.tim} >>> ENVIANT")
        if not msg[0:4] in ["read","wait"]:
            self.torn = not self.torn
        return publish_result
    
    def stop(self):
        self.pubnub.stop()
