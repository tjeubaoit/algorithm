# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        ans = []

        def dfs(node: TreeNode, s):
            if not node.left and not node.right:
                ans.append(s)
            if node.left:
                dfs(node.left, s+'->'+str(node.left.val))
            if node.right:
                dfs(node.right, s+'->'+str(node.right.val))

        dfs(root, str(root.val))
        return ans