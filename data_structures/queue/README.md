# Queue

## Explanation
The Queue is a linear data structure that orders its elements in FIFO (First In First Out) order. 

## Usage 

Add an item using:
```python
actionQueue = Queue()
actionQueue.add('Walk Left')
```

Remove the first item from the Queue by using **add()**: 
```python
actionQueue.remove()
```

You can use the removed item like so: 
```python
action = actionQueue.remove()
print(action)
```

You can view the first item **without** removing it by using **peek()**: 
```python
action = actionQueue.peek()
print(action)
```

Calling **remove()** on an empty Queue will raise an Exception: 
```python
Exception: Queue was empty. Cannot remove.
```

Calling **peek()** on an empty Queue will raise an Exception as well:
```python
Exception: Queue was empty. Cannot peek.
```