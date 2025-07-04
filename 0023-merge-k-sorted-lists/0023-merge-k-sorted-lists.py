# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)

        dummyHead = ListNode()
        heap = []

        cur = dummyHead

        for i in range(k):
            if lists[i]:
                heappush(heap, (lists[i].val, i, lists[i]))
        

        while heap:
            _, i, node = heappop(heap)
            cur.next = node
            cur = cur.next
            node = node.next
            if node:
                heappush(heap, (node.val, i, node))
        

        return dummyHead.next
