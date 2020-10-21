class Queue: 
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, data):
        node = QueueNode(data)
        if(self.last != None):
            self.last.next = node
        self.last = node
        if(self.first == None):
            self.first = self.last

    def remove(self):
        if self.first == None: 
            raise Exception('Queue is empty. Cannot remove.')    
        data = self.first.data
        self.first = self.first.next
        if self.first == None:
            self.last = None
        return data

    def peek(self):
        if self.empty():
            raise Exception('Queue is empty. Cannot peek.')
        return self.first
    
    def empty(self):
        return self.first == None

class QueueNode: 
    def __init__(self, data):
        self.data = data
        self.next = None