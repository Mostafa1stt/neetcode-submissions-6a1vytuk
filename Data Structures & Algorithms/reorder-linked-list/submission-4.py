# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ls = []
        temp = head
        while head != None:
            ls.append(head)
            head = head.next
        head = temp
        i = 0
        size = len(ls)
        j = size - 1
        while i < (size//2):
            ls[j].next = ls[i].next
            ls[i].next = ls[j]
            j-=1
            i+=1
        ls[i].next = None
