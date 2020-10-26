class Node: 
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right
    def empty(self):
        return self.left == None and self.right == None

def inorder_traverse(tree, result=None):
    if result == None:
        result = []
    if tree:
        inorder_traverse(tree.left, result)
        result.append(tree.name)
        inorder_traverse(tree.right, result)
    return result

def preorder_traverse(tree, result=None): 
    if result == None:
        result = []
    if tree:   
        result.append(tree.name)
        preorder_traverse(tree.left, result)
        preorder_traverse(tree.right, result)
    return result

def postorder_traverse(tree, result=None): 
    if result == None:
        result = []
    if tree:
        postorder_traverse(tree.left, result)
        postorder_traverse(tree.right, result)
        result.append(tree.name)
    return result
