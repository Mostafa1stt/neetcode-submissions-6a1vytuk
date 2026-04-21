# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        while head != None:
            last = head.next
            head.next = None
            cur = last
            while cur != None:
                cur = last.next
                last.next = head.next
                head.next = last
                last = cur
            head = head.next
