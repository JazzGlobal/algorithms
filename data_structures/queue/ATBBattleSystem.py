# Implementation of the Action Time Bar Battle System seen in Final Fantasy XIII
# 
# 
from math import floor
import queue

class Character:
    def __init__(self, move_list, speed):
        self.move_list = move_list
        self.speed = speed 
        self.move_queue = Queue() 

    def queue_move(self, move):
        self.move_queue.remove()
    
    def perform_move(self):
        move = self.move_queue.remove()
    
    def start(self):
        while (self.move_queue.empty() == False):
            seconds = floor((20 / self.speed))
            print(seconds)
            time.sleep(seconds)
            print('Perform action')

lightining = Character(['Attack', 'Defend', 'Escape'], 4)
lightining.queue_move(lightining.move_list[0])
lightining.queue_move(lightining.move_list[0])
lightining.queue_move(lightining.move_list[1])
lightining.queue_move(lightining.move_list[2])

lightining.start()