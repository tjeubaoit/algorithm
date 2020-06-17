# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        pre, i = dummy, 1
        while i < m:
            pre = head
            head = head.next
            i += 1

        # pbm: pointer before m
        # pm: pointer at m
        pbm, pm, nxt = pre, head, None
        while i <= n:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
            i += 1

        pbm.next = pre
        pm.next = head
        return dummy.next

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
    for i in range(0, 6):
        new_node = ListNode(i+1)
        node.next = new_node
        node = new_node

    ret = Solution().reverseBetween(fake.next, 2, 4)
    print_list(ret)
