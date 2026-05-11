/**
 * @lc id=206
 * @lc title=Reverse Linked List
 * @lc difficulty=Easy
 * @lc time=O(n)
 * @lc space=O(1)
 */
package linked_lists;

public class ReversedLinkedList {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        ListNode next;

        while (curr != null) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
}
