# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return self.val

    def __repr__(self):
        return self.val


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        fake: ListNode = ListNode(0)
        fake.next = head
        prev = fake
        while head:
            # Move next if curr val less than next val
            while head.next and head.val < head.next.val:
                head = head.next
            if not head.next:
                break

            # Set prev pointer back to head if necessary
            if prev.val > head.next.val:
                prev = fake

            # Move prev pointer to insertion position
            while prev.next.val < head.next.val:
                prev = prev.next

            # Remove current node
            tmp = head.next
            head.next = head.next.next

            # Insert new node
            tmp.next = prev.next
            prev.next = tmp
        return fake.next


def print_list(node: ListNode):
    while node:
        print(node.val, end='->' if node.next else '')
        node = node.next
    print()


if __name__ == '__main__':
    # nums = [-1, 5, 3, 4, 0]
    nums = [4, 2, 1, 3]
    head = ListNode(-1)
    curr = head
    for num in nums:
        node = ListNode(num)
        curr.next = node
        curr = node
    head = head.next
    print_list(head)

    head = Solution().insertionSortList(head)
    print_list(head)
