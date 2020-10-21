# Queue

## Explanation
The Queue is a linear data structure that orders its elements in FIFO (First In First Out) order. 

## Usage 

Add an item using:
```
actionQueue = Queue()
actionQueue.add('Walk Left')
```

Remove the first item from the Queue using: 
```
actionQueue.remove()
```

You can use the removed item like so: 
```
action = actionQueue.remove()
print(action)
```

You can view the first item **without** removing it by using **peek()**: 
```
action = actionQueue.peek()
print(action)
```

Calling **remove()** on an empty Queue will raise an Exception: 
```
Exception: Queue was empty. Cannot remove.
```

Calling **peek()** on an empty Queue will raise an Exception as well:
```
Exception: Queue was empty. Cannot peek.
```