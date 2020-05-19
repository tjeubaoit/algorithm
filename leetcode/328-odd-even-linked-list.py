# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        Use two sub list, one for odd node and one for even nodes
        :param head:
        :return:
        """
        odd = odd_head = ListNode(0)
        even = even_head = ListNode(0)
        idx = 1
        while head:
            if idx % 2 != 0:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            idx += 1
        odd.next = even_head.next
        even.next = None
        return odd_head.next


def print_list(head: ListNode):
    while head:
        print(head.val, end='->' if head.next else '')
        head = head.next
    print()


if __name__ == '__main__':
    fake = ListNode(-1)
    node = fake
    for i in range(1, 11):
        new_node = ListNode(i)
        node.next = new_node
        node = new_node

    ret = Solution().oddEvenList(head=fake.next)
    print_list(ret)
