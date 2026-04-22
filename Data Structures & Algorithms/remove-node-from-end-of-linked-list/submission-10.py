# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        cur = head
        tail = head
        counter = 0
        while counter < n:
            tail = tail.next
            counter += 1
        if tail == None:
            return head.next
        while tail.next != None:
            cur = cur.next
            tail = tail.next
        cur.next = cur.next.next
        return head