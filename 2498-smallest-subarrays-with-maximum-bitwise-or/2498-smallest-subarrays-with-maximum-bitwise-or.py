class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)

        set_bit_pos = [-1] * 32
        # max_set_bit_idx = -1
        max_or = 0
        res = [0] * n
        for i in range(n-1, -1, -1):
            cur = nums[i]
            max_or |= cur
            pos = 0
            while cur:
                if cur & 1:
                    set_bit_pos[pos] = i
                    # max_set_bit_idx = max(max_set_bit_idx, i)
                pos += 1
                
                cur >>= 1
            
            res[i] = max(1, max(set_bit_pos) - i  + 1)
            # max_set_bit_idx = max(set_bit_pos)
            # if max_set_bit_idx == -1:
            #     res.append(1)
            # else:
            #     res.append(max_set_bit_idx - i + 1)
        
        # res.reverse()
        return res