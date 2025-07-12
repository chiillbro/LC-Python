# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode()

        dummyNode.next = head

        prev_group_end = dummyNode

        while True:
            cur_group = prev_group_end
            for _ in range(k):
                cur_group = cur_group.next

                if not cur_group:
                    return dummyNode.next
                
            
            next_group_start = cur_group.next
            group_start = prev_group_end.next

            prev, cur = None, group_start

            while cur is not next_group_start:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            prev_group_end.next = prev
            group_start.next = next_group_start


            prev_group_end = group_start