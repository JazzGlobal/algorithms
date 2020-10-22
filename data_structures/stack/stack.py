class Stack:
    '''
    Stack implementation. Allows items to be added to the structure. Does not allow constant-time access to the "ith" item. 
    Allows constant time additions and removal of items. Does not require shifting when adding or removing items. 
    '''
    def __init__(self):
        self.top = None

    def pop(self):
        '''
        Checks if the Stack is empty, if not then remove the top item from the stack and return its value. 
        If the stack is empty then raise an exception.

        :return: Top item. 
        '''
        if (self.empty() == False):
            item = self.top.data
            self.top = self.top.next
            return item
        else: 
            raise Exception("Stack was empty. Cannot pop.")

    def push(self, data):
        '''
        Add an item to the top of the Stack. 

        :param data: Data contained within the StackNode. This can be almost anything desired.
        '''
        node = StackNode(data, self.top)
        self.top = node

    def peek(self):
        '''
        Checks if the Stack is empty, if not then return the data contained in top node. 
        If the Stack is empty, raise an exception.
        
        :return: Data contained within the top StackNode. 
        '''
        if self.empty() == False:
            return self.top.data
        else:
            raise Exception("Stack was empty. Cannot peek.")

    def empty(self):
        '''
        Returns whether or not the Stack is empty. 

        :return: Stack empty (True / False). 
        '''
        return self.top == None

class StackNode: 
    '''
    StackNode implementation. Used to point toward the data and next StackNode in the Stack. 

    :param data: Data contained within the StackNode. This can be almost anything. 
    :param next: Reference to the next StackNode within the Stack. 
    '''
    def __init__(self, data, next):
        self.data = data 
        self.next = next

