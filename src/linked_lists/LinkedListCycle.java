/**
 * @lc id=141
 * @lc title=Linked List Cycle
 * @lc difficulty=Easy
 * @lc time=O(n)
 * @lc space=O(1)
 */
package linked_lists;

public class LinkedListCycle {
    public boolean hasCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;

        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;

            if(slow == fast){
                return true;
            }
        }
        return false;

    }
}
