package sieunhan.algorithm.leetcode;

/**
 * @author <a href="https://github.com/tjeubaoit">tjeubaoit</a>
 */
public class AddTwoNumbers {

    static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {
            val = x;
        }
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int ex = 0;
        ListNode l3 = null;
        while (l1 != null || l2 != null) {
            int val = ex;
            if (l1 != null) {
                val += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                val += l2.val;
                l2 = l2.next;
            }
            ex = val / 10;
            val = val % 10;

            ListNode node = new ListNode(val);
            node.next = l3;
            l3 = node;
        }
        return l3;
    }

    public static void main(String[] args) {

    }
}
