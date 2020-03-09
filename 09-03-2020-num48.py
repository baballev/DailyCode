# Given two lists representing pre-order and in-order traversal of
# a tree, reconstruct the tree

test1 = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
test12 = ['d', 'b', 'e', 'a', 'f', 'c', 'g']

class Tree:
    left = None
    right = None
    def __init__(self, label):
        self.label = label


def tree(preorder, inorder):
    if not preorder and not inorder:
        return None
    if len(preorder) == len(inorder) == 1:
        return Tree(preorder[0])

    root = Tree(preorder[0])
    index = inorder.index(root.label)
    root.left = tree(preorder[1: index + 1], inorder[0: index])
    root.right = tree(preorder[1 + index:], inorder[index + 1:])

    return root

print(tree(test1, test12).label)

