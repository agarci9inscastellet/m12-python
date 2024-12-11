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
    response=False
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
            self.ready=int(message.message.split(":")[1])
            self.mytorn = self.tim > self.ready 

            if code=="wait":
                self.send( f"ready:{self.tim}") 
        elif code in ["resu"]:
            self.response=message.message
        else:
            self.jugada=message.message
            #print("TOOORN ",self.torn)


    def response_opponent(self,msg=""):
        self.jugada = False
        while not self.response:
            time.sleep(0.2)
        return self.response
                
    def wait_opponent(self,msg=""):
        self.response = False

        msg=f"Esperant jugada de {self.contrincant_id}"
        print(msg)
        while not self.jugada:
            time.sleep(0.2)
                
        self.response = False
        return self.jugada
  
    def send(self, msg):

        subscribed_channels = self.pubnub.get_subscribed_channels()
        publish_result = self.pubnub.publish().channel( subscribed_channels[0]).message(msg).sync() 
        #print (f"SEND {msg} {subscribed_channels[0]}... {self.ready} - {self.tim} >>> ENVIANT")
        #if not msg[0:4] in ["read","wait","resu"]:
            #self.torn = not self.torn
        

        return publish_result
    


    def stop(self):
        self.pubnub.stop()
