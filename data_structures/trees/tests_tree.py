import unittest
from tree import Node
import tree 

# Tests
class TestNode(unittest.TestCase):
    def test_instantiation(self):
        # Arrange 
        test_node = Node('Parent', None, None)
        # Act
            # None
        # Assert
        self.assertEqual('Parent', test_node.name)

    # Inorder Traverse tests.
    def test_inorder_traverse_emptytree(self):
        # Arrange
        test_node = Node(0, None, None)
        # Act
        result = tree.inorder_traverse(test_node)
        print(result)
        # Assert
        self.assertEqual([0], result)
    def test_inorder_traverse(self):
        # Arrange
        test_node = Node(0, Node(1, Node(3, None, None),None), Node(2, None, Node(4, None, None)))
        # Act
        result = tree.inorder_traverse(test_node)
        # Assert
        self.assertEqual([3,1,0,2,4], result)
    def test_inorder_traverse_multibranch(self):
        # Arrange
        test_node = Node(1, Node(2, Node(4, None, None), Node(5, None, None)), Node(3, None, None))
        # Act
        result = tree.inorder_traverse(test_node)
        # Assert
        self.assertEqual([4,2,5,1,3], result)
    def test_inorder_traverse_multibranch2(self):
        # Arrange
        test_node = Node(0, Node(1, Node(3, None, None), Node(5, None,None)),  Node(2, Node(4, None, None), Node(6, None, None)))
        # Act
        result = tree.inorder_traverse(test_node)
        # Assert
        self.assertEqual([3,1,5,0,4,2,6], result)
    
    # Preorder Tree Traversal tests.
    def test_preorder_traverse(self):
        # Arrange
        test_node = Node(0, Node(1, Node(3, None, None),None), Node(2, None, Node(4, None, None)))
        # Act
        result = tree.preorder_traverse(test_node)
        # Assert
        self.assertEqual([0,1,3,2,4], result)
    def test_preorder_traverse_multibranch(self):
        # Arrange
        test_node = Node(1, Node(2, Node(4, None, None), Node(5, None, None)), Node(3, None, None))
        # Act
        result = tree.preorder_traverse(test_node)
        # Assert
        self.assertEqual([1,2,4,5,3], result)

    # Postorder Tree Traversal tests.
    def test_postorder_traverse(self):
        # Arrange
        test_node = Node(0, Node(1, Node(3, None, None),None), Node(2, None, Node(4, None, None)))
        # Act
        result = tree.postorder_traverse(test_node)
        # Assert
        self.assertEqual([3,1,4,2,0], result)
    def test_postorder_traverse_multibranch(self):
        # Arrange
        test_node = Node(1, Node(2, Node(4, None, None), Node(5, None, None)), Node(3, None, None))
        # Act
        result = tree.postorder_traverse(test_node)
        # Assert
        self.assertEqual([4,5,2,3,1], result)

if __name__ == '__main__':
    unittest.main()