# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
# Difficulty: Medium
#
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#
# Example:
#   Input: l1 = [2,4,3], l2 = [5,6,4]
#   Output: [7,0,8]  (342 + 465 = 807)
#
# Time Complexity: O(max(m, n))
# Space Complexity: O(max(m, n))

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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, digit = divmod(val, 10)
            current.next = ListNode(digit)
            current = current.next
        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    l1 = list_to_nodes([2, 4, 3])
    l2 = list_to_nodes([5, 6, 4])
    assert nodes_to_list(sol.addTwoNumbers(l1, l2)) == [7, 0, 8]

    l1 = list_to_nodes([0])
    l2 = list_to_nodes([0])
    assert nodes_to_list(sol.addTwoNumbers(l1, l2)) == [0]

    l1 = list_to_nodes([9, 9, 9, 9, 9, 9, 9])
    l2 = list_to_nodes([9, 9, 9, 9])
    assert nodes_to_list(sol.addTwoNumbers(l1, l2)) == [8, 9, 9, 9, 0, 0, 0, 1]
    print("All tests passed!")
