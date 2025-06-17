# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)

        # the solution is just like how we add two big numbers on paper

        # 2 4 5 5
        # 8 5 9 3

        # 1 1      -> carries from the previous addition results
        #---------
        #11 0 4 8   #here for 9+5=14, we carried the 1 to the next addition coming up and same with the 4+5+ (1 carry from previous addition)=10, 2+8+(1 carry from the prev add)=11
        p, q, cur = l1, l2, dummyNode

        carry = 0 # this represents the carry that we should take forward to add to the next addition for accumulating correct digit of the integer

        while p or q:
            digit1, digit2 = p.val if p else 0, q.val if q else 0

            cur_sum = digit1 + digit2 + carry

            # print("cur_sum before", cur_sum)
            carry = cur_sum // 10
            # print("carry", carry)

            # print("cur_sum after", cur_sum)

            cur.next = ListNode(cur_sum % 10)
            cur = cur.next

            p = p.next if p else None
            q = q.next if q else None
        
        if carry:
            cur.next = ListNode(carry)
        
        return dummyNode.next