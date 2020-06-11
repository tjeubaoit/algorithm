# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        nxt, pre = None, dummy

    @staticmethod
    def reverse_linked_list(head: ListNode):
        nxt, pre = None, None
        while head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        return pre


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

    ret = Solution().reverseBetween(fake.next, 2, 4)
    print(ret)
