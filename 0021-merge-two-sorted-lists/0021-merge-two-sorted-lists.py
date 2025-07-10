# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()

        cur = dummyNode

        l1, l2 = list1, list2

        while l1 and l2:
            val = None

            if l1.val < l2.val:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next

            
            new_node = ListNode(val)

            cur.next = new_node

            cur = new_node
        
        while l1:
            new_node = ListNode(l1.val)
            l1 = l1.next

            cur.next = new_node

            cur = new_node
        
        while l2:
            new_node = ListNode(l2.val)
            l2 = l2.next

            cur.next = new_node

            cur = new_node
        
        return dummyNode.next
        