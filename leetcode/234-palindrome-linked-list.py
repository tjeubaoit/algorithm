# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        left = head
        right = self.reverse_linked_list(slow)
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

    @staticmethod
    def reverse_linked_list(head: ListNode):
        nxt, pre = None, None
        node = head
        while node:
            nxt = node.next
            node.next = pre
            pre = node
            node = nxt
        return pre


def print_list(head: ListNode):
    node = head
    while node:
        print(node.val, end='->' if node.next else '')
        node = node.next
    print()


if __name__ == '__main__':
    fake = ListNode(-1)
    node = fake
    for val in [1, 2, 2, 3, 2, 1]:
        new_node = ListNode(val)
        node.next = new_node
        node = new_node
    print_list(fake.next)
    # head = Solution.reverse_linked_list(fake.next)
    # print_list(head)

    ret = Solution().isPalindrome(fake.next)
    print(ret)
