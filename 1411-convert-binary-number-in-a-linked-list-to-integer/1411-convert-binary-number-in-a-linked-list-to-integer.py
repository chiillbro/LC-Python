# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        cur = head

        i = 0

        while cur:
            i += 1
            cur = cur.next
        
        i -= 1
        cur = head
        num = 0

        while cur:
            num += (1 << (i)) * cur.val
            i -= 1
            cur = cur.next
        
        return num