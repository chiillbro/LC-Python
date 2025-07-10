# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        stack, node = [], head

        while node:
            stack.append(node)
            node = node.next

        
        start, cnt = head, 0

        while cnt < len(stack) - 1:
            temp = start.next
            node = stack.pop()

            start.next = node
            node.next = temp

            start = temp

            cnt += 1
        
        start.next = None
        