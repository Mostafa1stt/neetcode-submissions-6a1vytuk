# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        rev = None
        net = head.next
        while head != None:
            net = head.next
            head.next = rev
            rev = head
            head = net
        if n !=1:
            lol = rev   
            for i in range(1,n-1):
                rev = rev.next
            rev.next = rev.next.next
        else:
            lol = rev.next
        head = None
        net = lol.next
        while lol != None:
            net = lol.next
            lol.next = head
            head = lol
            lol = net
        return head