from queue import SimpleQueue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode):
        if not root: return [0]
        q = SimpleQueue()
        q.put(root)
        ans = []
        while not q.empty():
            total, size = 0, q.qsize()
            for _ in range(size):
                node = q.get()
                total += node.val
                if node.left: q.put(node.left)
                if node.right: q.put(node.right)
            ans.append(total/size)
        return ans
