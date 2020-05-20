from queue import SimpleQueue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        q = SimpleQueue()
        q.put(root)
        dep = 0
        while not q.empty():
            for _ in range(0, q.qsize()):
                node = q.get()
                if not node.left and not node.right:
                    return dep+1
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            dep += 1
