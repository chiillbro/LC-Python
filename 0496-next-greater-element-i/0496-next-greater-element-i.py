class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, hashmap = [], defaultdict(int)

        for i in range(len(nums2) - 1, -1, -1):
            num = nums2[i]

            while stack and stack[-1] <= num:
                stack.pop()
            

            if stack:
                hashmap[num] = stack[-1]
            else:
                hashmap[num] = -1
                
            stack.append(num)
        
        return [hashmap[num] for num in nums1]

