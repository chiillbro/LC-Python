class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, hashmap = [], defaultdict(int)

        for i in range(len(nums2) - 1, -1, -1):
            num = nums2[i]

            while stack:
                if stack[-1] > num:
                    hashmap[num] = stack[-1]
                    stack.append(num)
                    break
                else:
                    stack.pop()
            
            if not stack:
                hashmap[num] = -1
                stack.append(num)
        
        return [hashmap[num] for num in nums1]

