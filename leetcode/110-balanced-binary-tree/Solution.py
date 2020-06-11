# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def height(node):
            if not node:
                return 0
            left = height(node.left) if node.left else 0
            right = height(node.right) if node.right else 0

            if abs(left - right) > 1:
                return -2
            return 1 + max(left, right)

        ret = height(root)
        return ret > 0


if __name__ == '__main__':
    pass
