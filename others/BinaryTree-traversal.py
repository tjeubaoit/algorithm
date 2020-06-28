class BstTreeTraversal:
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
                vals.append(current.val)

                # We have visited the node and its left
                # subtree. Now, it's right subtree's turn
                current = current.right
            else:
                break
        return vals