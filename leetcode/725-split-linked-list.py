# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, root: ListNode, k: int):
        """
        Split list to k parts with len/k items
        Add one item to each part and decrease remainder to 1
        until remainder equals 0
        """
        head, ct = root, 0
        while head:
            ct += 1
            head = head.next

        length, remainder = divmod(ct, k)
        node, ans = root, []
        for i in range(k):
            head = node
            for _ in range(1, length + (i < remainder)):
                if not node: break
                node = node.next
            if node:
                tmp = node.next
                node.next = None
                node = tmp
            ans.append(head)
        return ans


def print_list(head: ListNode):
    while head:
        print(head.val, end='->' if head.next else '')
        head = head.next
    print()


if __name__ == '__main__':
    fake = ListNode(-1)
    node = fake
    for i in range(0, 10):
        new_node = ListNode(i+1)
        node.next = new_node
        node = new_node

    ret = Solution().splitListToParts(fake.next, 4)
    for head in ret:
        print_list(head)
