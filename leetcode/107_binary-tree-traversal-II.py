from queue import SimpleQueue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if not root: return []
        q = SimpleQueue()
        q.put(root)

        ans = []
        while not q.empty():
            ret = []
            for _ in range(0, q.qsize()):
                node = q.get()
                ret.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            ans.append(ret)
        return reversed(ans)

