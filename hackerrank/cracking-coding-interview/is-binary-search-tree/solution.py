""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    return checkBST0(root, 0, 10000)

def checkBST0(root, min_val, max_val):
    if root is None: 
        return True
  
    if root.data <= min_val or root.data >= max_val:
        return False
  
    if not checkBST0(root.left, min_val, min(max_val, root.data)):  
        return False
  
    return checkBST0(root.right, max(min_val, root.data), max_val) 