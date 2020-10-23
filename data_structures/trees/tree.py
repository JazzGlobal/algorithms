class Node: 
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right
    def empty(self):
        return self.left == None and self.right == None

def preorder_traverse(tree, result):
    if result == None:
        result = []
    if tree:
        preorder_traverse(tree.left, result)
        result.append(tree.name)
        preorder_traverse(tree.right, result)
    return result