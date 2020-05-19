# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        return self.solution1(headA, headB)

    def solution1(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        pa, pb = headA, headB
        tailA, tailB = None, None
        while pa != pb:
            if pa.next:
                pa = pa.next
            else:
                # Move to head of list B
                tailA = pa
                pa = headB
                if tailB and tailA != tailB:
                    return None
            if pb.next:
                pb = pb.next
            else:
                # Move to head of list A
                tailB = pb
                pb = headA
                if tailA and tailA != tailB:
                    return None
        return pa

    def solution2(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        pa, pb = headA, headB
        lenA, lenB = 0, 0
        # Move list A to end and count number items
        while pa:
            pa = pa.next
            lenA += 1
        # Move list B to end and count number items
        while pb:
            pb = pb.next
            lenB += 1

        pa, pb = headA, headB
        # Larger list will move first until remain items of two lists are equals
        while lenA > lenB:
            pa = pa.next
            lenA -= 1
        while lenB > lenA:
            pb = pb.next
            lenB -= 1
        while pa and pa != pb:
            pa = pa.next
            pb = pb.next
        return pa


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
