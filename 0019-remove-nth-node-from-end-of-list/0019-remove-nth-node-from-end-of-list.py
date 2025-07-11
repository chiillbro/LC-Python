# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        ahead, behind = head, dummyNode

        for _ in range(n):
            ahead = ahead.next
        
        while ahead:
            ahead = ahead.next
            behind = behind.next
        
        behind.next = behind.next.next

        return dummyNode.next
        
