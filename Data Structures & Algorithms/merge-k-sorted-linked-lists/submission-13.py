# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        msorted = ListNode(0)
        head = msorted
        while True:
            minner = None
            point = -1
            for i in range(len(lists)):
                if lists[i] is None:
                    continue
                if minner is None or minner.val > lists[i].val:
                    minner = lists[i]
                    point = i
            if minner is None:
                break
            head.next = minner
            head = head.next
            lists[point] = lists[point].next
        return msorted.next
