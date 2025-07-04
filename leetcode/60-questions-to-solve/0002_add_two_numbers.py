from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0  # 繰り上がりの数を保持

        while l1 or l2 or carry != 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry

            digit = sum % 10  # digit of 1
            carry = sum // 10  # digit of 10

            current.next = ListNode(digit)
            current = current.next

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        return dummy.next
