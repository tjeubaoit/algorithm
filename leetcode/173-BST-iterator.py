# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.current = root
        self.stack = []
        self._leftMostInOrder(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        current = self.stack.pop()
        if current.right:
            self._leftMostInOrder(current.right)
        return current.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack
    
    def _leftMostInOrder(self, root):
        while root is not None:
            self.stack.append(root)
            root = root.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()