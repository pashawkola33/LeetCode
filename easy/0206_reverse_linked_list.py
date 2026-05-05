# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# Difficulty: Easy
#
# Given the head of a singly linked list, reverse the list, and return the
# reversed list.
#
# Example:
#   Input: head = [1,2,3,4,5]
#   Output: [5,4,3,2,1]
#
# Time Complexity: O(n)
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev


if __name__ == "__main__":
    sol = Solution()
    head = list_to_nodes([1, 2, 3, 4, 5])
    assert nodes_to_list(sol.reverseList(head)) == [5, 4, 3, 2, 1]

    head = list_to_nodes([1, 2])
    assert nodes_to_list(sol.reverseList(head)) == [2, 1]

    assert sol.reverseList(None) is None
    print("All tests passed!")
