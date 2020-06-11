# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        i = 0
        fast, slow = head, head
        while i < k and fast:
            fast = fast.next
            i += 1
        if i >= k:


def print_list(head: ListNode):
    while head:
        print(head.val, end='->' if head.next else '')
        head = head.next
    print()


if __name__ == '__main__':
    fake = ListNode(-1)
    node = fake
    for i in range(0, 5):
        new_node = ListNode(i+1)
        node.next = new_node
        node = new_node

    ret = Solution().rotateRight(fake.next, 3)
    print(ret)
