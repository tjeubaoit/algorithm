# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        vals = []

        def inOrderTraversal(node: TreeNode):
            if node.left:
                inOrderTraversal(node.left)
            vals.append(node.val)
            if node.right:
                inOrderTraversal(node.right)

        inOrderTraversal(root)

        for i in range(len(vals) - 1):
            if vals[i] >= vals[i + 1]:
                return False
        return True
