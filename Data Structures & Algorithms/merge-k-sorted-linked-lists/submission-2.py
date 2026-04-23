class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while True:
            minner = None
            point = -1

            for i in range(len(lists)):
                if lists[i] is None:
                    continue
                if minner is None or lists[i].val < minner.val:
                    minner = lists[i]
                    point = i

            if minner is None:
                break  # all lists are empty

            # append to result
            tail.next = minner
            tail = tail.next

            # move pointer in that list
            lists[point] = lists[point].next

        return dummy.next