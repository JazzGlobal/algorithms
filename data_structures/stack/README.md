# Stack

## Explanation
The Stack is a linear data structure that orders its elements in either LIFO (Last In First Out). 

## Usage 

Add an item using. Almost any value / object can take the place of "Hello World":
```
messageStack = Stack()
messageStack.push('Hello World!')
```

Pop an item from the Stack using: 
```
messageStack.pop()
```

You can use the "popped" item like so: 
```
message = messageStack.pop()
print(message)
```

You can view the top item **without** popping by using **peek()**: 
```
message = messageStack.peek()
print(message)
```

Calling **pop()** on an empty Stack will raise an Exception: 
```
Exception: Stack was empty. Cannot pop.
```

Calling **peek()** on an empty Stack will raise an Exception as well:
```
Exception: Stack was empty. Cannot peek.
```