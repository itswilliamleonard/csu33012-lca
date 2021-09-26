# PYTHON 3.9x
# LOWEST COMMON ANCESTOR
# LIAM O LIONAIRD [19335530]
# 25/09/21

# written with Vim, submitted using git command-line!

class Node:
    def __init__(self):
        self.left = None # we can set these to a new Node object
        self.right = None # but we don't have to test here.....

def lowestCommonAncestor(node1, node2, root):
    # adapting code from LCA.java...

    if node1 == root and node1 == root:
        return root

    leftLCA = lowestCommonAncestor(node1, node2, root.left)
    rightLCA = lowestCommonAncestor(node1, node2, root.right)

    if leftLCA != None and rightLCA != None:
        return root

    if leftLCA is None:
        return rightLCA
    else:
        return leftLCA

