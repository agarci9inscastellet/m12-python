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
    
    num_players = 3
    players = [tim]

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

        while len(self.players) < self.num_players:
            self.send( f"_#@w:{self.tim}") 
            print (f"wait ... {self.ready} - {self.tim} >>> {self.players} >>> Esperant connexió")
            time.sleep(0.5)

    def receiver(self, message):

        if (message.publisher == self.pubnub.config.user_id):
            return
                
        #print("REBUT", message.publisher, message.message," --- ",self.torn ," / ",self.mytorn)

        self.contrincant_id=message.publisher
        
        code = message.message[0:4]
      
        if code in ["_#@r","_#@w"]:
           # if not self.ready:
            #print (f"{code} ... {self.ready} - {self.tim} >>> Connetats amb {message.publisher}")
            #self.ready=int(message.message.split(":")[1])
            #self.mytorn = int(self.tim > self.ready) 
            tim = int(message.message.split(":")[1])
            #print("---",message.message)
            if (tim not in self.players):
                self.players.append(tim)
                print(self.players)
                
            

            if code=="_#@w":
                self.send( f"_#@r:{self.tim}") 
                
                

        else:
            if (code == "_#@n"):
                self.torn = not self.torn
                #print("oponent perd el torn")

            else:
                self.jugada=message.message
                
    def play_opponent(self,msg=""):     
        self.jugada = False             
        while not self.jugada:
            time.sleep(0.2)
        
        return self.jugada


    def play_opponentxx(self,msg=""):                  
        if self.torn != self.mytorn:
            if not msg:
                msg=f"Esperant jugada de {self.contrincant_id}"
            print(msg)
            while self.torn != self.mytorn:
                print("while ",self.torn ," / ",self.mytorn)

                time.sleep(0.2)
            return self.jugada
        return False
               
    def played_opponent(self):
         if self.jugada:
             ret = self.jugada
             self.jugada = False
             return ret
         return False

    
    def is_my_turn(self):
        time.sleep(0.5)
        return  self.torn == self.mytorn

        
    def send(self, msg):

        subscribed_channels = self.pubnub.get_subscribed_channels()
        publish_result = self.pubnub.publish().channel( subscribed_channels[0]).message(msg).sync() 
        #print (f"SEND {msg} {subscribed_channels[0]}... {self.ready} - {self.tim} >>> ENVIANT")
        # if not msg[0:4] in ["_#@r","_#@w"]:
        #     #self.torn = not self.torn
        #     a=0
        return publish_result
    
    
    def next_player(self):
        self.send("_#@n") 
        self.torn = not self.torn
        #print("perdo el torn")

    
    def stop(self):
        self.pubnub.stop()
