# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        st = [(root, 0)]
        while st:
            node, xsum = st.pop()
            xsum += node.val
            if xsum == sum and not node.left and not node.right:
                return True
            if node.left:
                st.append((node.left, xsum))
            if node.right:
                st.append((node.right, xsum))
        return False
