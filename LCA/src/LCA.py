# PYTHON 3.9x
# LOWEST COMMON ANCESTOR
# LIAM O LIONAIRD [19335530]
# v1: 25/09/21
# v2: 14/10/21

# written with Vim, submitted using git command-line!

import unittest

class Node:
    def __init__(self):
        self.left = None # when testing, set these to a Node object
        self.right = None

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

def lowestCommonAncestor(node1, node2, root):
    # adapting code from LCA.java...

    if root == None:
        return None
    if node1 == root or node2 == root:
        return root

    leftLCA = lowestCommonAncestor(node1, node2, root.getLeft())
    rightLCA = lowestCommonAncestor(node1, node2, root.getRight())

    if leftLCA != None and rightLCA != None:
        return root

    if leftLCA is None:
        return rightLCA
    else:
        return leftLCA

class testLCA(unittest.TestCase):

    def test_node(self):
        a = Node()
        b = Node()
        c = Node()
        a.setLeft(b)
        a.setRight(c)
        self.assertEqual(a.getLeft(), b)
        self.assertEqual(a.getRight(), c)

    def test_LCA(self):
        # Arranging these nodes into the following tree:
        #        A
        #       / \
        #      B   C
        #     / \   \
        #    D   E   F
        #       /
        #      G
        a = Node()
        b = Node()
        c = Node()
        d = Node()
        e = Node()
        f = Node()
        g = Node()
        a.setLeft(b)
        a.setRight(c)
        b.setLeft(d)
        b.setRight(e)
        c.setRight(f)
        e.setLeft(g)

        self.assertEqual(a, lowestCommonAncestor(a, a, a))
        self.assertEqual(a, lowestCommonAncestor(b, c, a))
        self.assertEqual(a, lowestCommonAncestor(d, f, a))
        self.assertEqual(b, lowestCommonAncestor(d, g, a))

if __name__ == '__main__':
    unittest.main() # Runs the tests
