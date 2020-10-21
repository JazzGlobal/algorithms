class Stack:
    def __init__(self):
        self.top = None

    def pop(self):
        if (self.empty() == False):
            item = self.top.data
            self.top = self.top.next
            return item
        else: 
            raise Exception("Stack was empty. Cannot pop.")

    def push(self, data):
        node = StackNode(data, self.top)
        self.top = node

    def peek(self):
        if self.empty() == False:
            return self.top.data
        else:
            raise Exception("Stack was empty. Cannot peek.")

    def empty(self):
        return self.top == None

class StackNode: 
    def __init__(self, data, next):
        self.data = data 
        self.next = next 