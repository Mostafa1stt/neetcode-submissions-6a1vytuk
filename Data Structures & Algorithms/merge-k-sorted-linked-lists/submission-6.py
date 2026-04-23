# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists :
            return None

        msorted = ListNode(0)
        head = msorted
        while True:
            minner,point = lists[0],0
            for i in range(len(lists)):
                if lists[i] == None:
                    continue
                if minner == None or minner.val > lists[i].val:
                    minner = lists[i]
                    point = i
            if minner == None:
                break
            head.next = minner
            head = head.next
            lists[point] = lists[point].next
        return msorted.next
