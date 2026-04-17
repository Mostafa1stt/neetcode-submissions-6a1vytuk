class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        rev_head = None
        while cur != None:
            cur = cur.next
            head.next = rev_head
            rev_head = head
            head = cur
        return rev_head