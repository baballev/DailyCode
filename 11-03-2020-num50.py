# Given the root of a binary tree within the one leafs are integer and
# internal nodes are operators, return the result of the expression.

# We can apply symetrical traversal within the tree to get the expression:
class Node:
    def __init__(self, label, left=None, right=None):
        self.label = label
        self.right = right
        self.left = left

def sym_trav(root):
    if root.left == root.right == None:
        return root.label
    l = sym_trav(root.left)
    r = sym_trav(root.right)
    if root.label == '+':
        return l + r
    elif root.label == '-':
        return l - r
    elif root.label == '*':
        return l*r
    elif root.label == '/':
        return l/r
    else:
        print("An  error occured readint the binary tree")
        return 0

