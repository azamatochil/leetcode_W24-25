# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next or not head:
            return

        ptr = head.next
        head = ptr.next
        ptr.next = head
        head = ptr

        self.swapPairs(head.next.next)