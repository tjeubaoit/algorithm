# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Iterative function for inOrder tree traversal
    def inOrder(self, root):
        # Set current to root of binary tree
        current = root
        stack = []  # initialize stack
        vals = []

        while True:
            # Reach the left most Node of the current Node
            if current is not None:
                # Place pointer to a tree node on the stack
                # before traversing the node's left subtree
                stack.append(current)
                current = current.left

            # BackTrack from the empty subtree and visit the Node
            # at the top of the stack; however, if the stack is
            # empty you are done
            elif stack:
                current = stack.pop()
                vals.append(current.data)

                # We have visited the node and its left
                # subtree. Now, it's right subtree's turn
                current = current.right
            else:
                break
        return vals

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        vals1 = self.inOrder(root1)
        vals2 = self.inOrder(root2)

        ans = [0]*(len(vals1) + len(vals2))
        i, j, k = 0, 0, 0
        while i < len(vals1) and j < len(vals2):
            if vals1[i] < vals2[j]:
                ans[k] = vals1[i]
                i += 1
            else:
                ans[k] = vals2[j]
                j += 1
            k += 1
        while i < len(vals1):
            ans[k] = vals1[i]
            k += 1
            i += 1
        while j < len(vals2):
            ans[k] = vals2[j]
            k += 1
            j += 1
        return ans
