# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# Difficulty: Easy
#
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by
# splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
#
# Example:
#   Input: list1 = [1,2,4], list2 = [1,3,4]
#   Output: [1,1,2,3,4,4]
#
# Time Complexity: O(m + n)
# Space Complexity: O(1)

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def list_to_nodes(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def nodes_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2
        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    l1 = list_to_nodes([1, 2, 4])
    l2 = list_to_nodes([1, 3, 4])
    assert nodes_to_list(sol.mergeTwoLists(l1, l2)) == [1, 1, 2, 3, 4, 4]

    assert nodes_to_list(sol.mergeTwoLists(None, None)) == []

    l2 = list_to_nodes([0])
    assert nodes_to_list(sol.mergeTwoLists(None, l2)) == [0]
    print("All tests passed!")
