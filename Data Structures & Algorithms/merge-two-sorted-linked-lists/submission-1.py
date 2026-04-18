# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tail = None 
        cur_1 = list1
        cur_2 = list2
        head = None
        while cur_1 != None and cur_2 != None:
            if cur_1.val < cur_2.val:
                if tail == None:
                    tail = cur_1
                    head = tail
                else:
                    tail.next = cur_1
                    tail = cur_1
                cur_1 = cur_1.next
            else:
                if tail == None:
                    tail = cur_2
                    head = tail
                else:
                    tail.next = cur_2
                    tail = cur_2
                cur_2 = cur_2.next
                
        if cur_1 != None:
            if tail == None:
                tail = cur_1
                head = tail
            else:
                tail.next = cur_1

        if cur_2 != None:
            if tail == None:
                tail = cur_2
                head = tail
            else:
                tail.next = cur_2
            
        return head