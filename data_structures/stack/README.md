# Stack

## Explanation
The Stack is a linear data structure that orders its elements in LIFO (Last In First Out) order. 

## Usage 

Add an item using **add()** (Almost any value / object can take the place of "Hello World"):
```python
messageStack = Stack()
messageStack.push('Hello World!')
```

Pop an item from the Stack using: 
```python
messageStack.pop()
```

You can use the "popped" item like so: 
```python
message = messageStack.pop()
print(message)
```

You can view the top item **without** popping by using **peek()**: 
```python
message = messageStack.peek()
print(message)
```

Calling **pop()** on an empty Stack will raise an Exception: 
```python
Exception: Stack was empty. Cannot pop.
```

Calling **peek()** on an empty Stack will raise an Exception as well:
```python
Exception: Stack was empty. Cannot peek.
```