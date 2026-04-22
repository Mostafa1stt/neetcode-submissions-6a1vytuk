# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next ==None:
            return None
        tail = head
        lol = head
        counter = 0
        while tail != None:
            counter += 1
            tail = tail.next
        target = counter - n
        if target == 0:
            head = head.next
            return head
        else:
            for i in range(target-1):
                head = head.next
            head.next = head.next.next
            return lol
            
            
