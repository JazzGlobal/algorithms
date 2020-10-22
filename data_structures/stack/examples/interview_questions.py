# Exercises found within PAGE 98 - 99 of Cracking the Coding Interview 6th Edition by Gayle McDowell. 
from stack import Stack

# 3.3: Stack of plates 
# Implement a data structure composed of Stacks. This data structure must create a new Stack once one gets too full. 
# SetOfStacks.push() and SetofStacks.pop() shoulkd behave as they do in Stack. 

class SetOfStacks():
    def __init__(self, threshold):
        self.threshold = threshold
        self.stacks = []
        self.currentCount = 0

    def push(self, data):
        if len(self.stacks) < 1:
            # Create new Stack and add to list
            stack = Stack()
            stack.push(data)
            self.stacks.append(stack)
        elif self.currentCount >= self.threshold:
            # Create new Stack and prepend it to list.
            stack = Stack()
            stack.push(data)
            self.stacks.insert(0, stack)
            self.currentCount = 0
        else: 
            # Push data to current Stack.
            self.stacks[0].push(data)
            self.currentCount += 1

    def pop(self):
        if self.empty() == True: 
            raise Exception('SetOfStacks was empty. Can not pop.')
        data = self.stacks[0].pop()
        if self.stacks[0].empty() == True: # If this Stack.pop() would result in an empty Stack. Remove it from the SetOfStacks.
            self.stacks.pop(0)
        return data

    def peek(self):
        if self.empty() == True: 
            raise Exception('SetOfStacks was empty. Can not peek.')
        return self.stacks[0].peek()
    
    def popAt(self, index):
        if self.empty() == True: 
            raise Exception('SetOfStacks was empty. Can not pop.')
        data = self.stacks[index].pop()
        if(self.stacks[index].empty()): # If this Stack.pop() would result in an empty Stack. Remove it from the SetOfStacks.
            self.stacks.pop(index)

    def peekAt(self, index):
        if self.empty() == True: 
            raise Exception('SetOfStacks was empty. Can not peek.')
        return self.stacks[index].peek()

    def empty(self):
        return len(self.stacks) < 1