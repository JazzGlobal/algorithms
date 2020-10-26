# Tree / Node

## Explanation
### Tree
A tree is an abstract data type mostly used to depict hierarchical relationships among its data. 
### Node
A node represents a piece of data within a tree. 

Example: https://github.com/JazzGlobal/algorithms/blob/master/data_structures/trees/test_inorder_traverse_multibranch.png

## Usage 

You would create the above tree with:

```
tree = Node(1, Node(2, Node(4, None, None), Node(5, None, None)), Node(3, None, None))
```

## Traversal
You can traverse the tree with the following methods: 

### Depth First:
#### Inorder
```python
print(inorder_traversal(tree))
# returns [4,2,5,1,3]
```
#### Preorder
```python
print(preorder_traversal(tree))
# returns [1,2,4,5,3]
```
#### Postorder
```python
print(postorder_traversal(tree))
# returns [4,5,2,3,1]
```
