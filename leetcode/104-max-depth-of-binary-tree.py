
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import SimpleQueue

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return self.solution2(root)
        
    # DFS
    def solution1(self, root: TreeNode) -> int:
        st = [(root, 1)]
        ans = 0
        while st:
            node, dep = st.pop()
            ans = max(ans, dep)
            if node.left:
                st.append((node.left, dep + 1))
            if node.right:
                st.append((node.right, dep + 1))
        return ans
    
    # BFS
    def solution2(self, root: TreeNode) -> int:
        q = SimpleQueue()
        q.put(root)
        ans = 0
        while not q.empty():
            for _ in range(q.qsize()):
                node = q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            ans += 1
        return ans