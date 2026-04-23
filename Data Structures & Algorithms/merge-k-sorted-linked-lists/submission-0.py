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
                if minner == None:
                    minner,point = lists[i],i 
                if minner.val > lists[i].val:
                    minner = lists[i]
                    point = i
            if lists[point] == None:
                break
            lists[point] = lists[point].next
            minner.next = msorted.next
            msorted.next = minner
            msorted = msorted.next
            print(msorted.val)
        return head.next
