# Implementation of the Action Time Bar Battle System seen in Final Fantasy XIII
# 
# 
from math import floor
from queue import Queue
import time 


class Character:
    def __init__(self, move_list, speed):
        self.move_list = move_list
        self.speed = speed 
        self.move_queue = Queue() 

    def queue_move(self, move):
        self.move_queue.add(move)
    
    def perform_move(self):
        move = self.move_queue.remove()
    
    def start(self):
        while (self.move_queue.empty() == False):
            seconds = floor((20 / self.speed))
            time.sleep(seconds)
            action = self.move_queue.remove()
            print('Performing Action:', action)

lightining = Character(['Attack', 'Ruin', 'Blitz'], 7)
lightining.queue_move(lightining.move_list[0])
lightining.queue_move(lightining.move_list[0])
lightining.queue_move(lightining.move_list[1])
lightining.queue_move(lightining.move_list[2])

lightining.start()

# Action interval = 2 OR floor(20 / 7)
# Every 2 seconds Lightining's queue trigger the next move. 

# prints the following: 
# Performing Action: Attack
# Performing Action: Attack
# Performing Action: Ruin
# Performing Action: Blitz
