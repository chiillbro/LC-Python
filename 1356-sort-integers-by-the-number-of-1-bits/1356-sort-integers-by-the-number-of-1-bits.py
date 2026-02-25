class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def sort_func(a, b):

            from functools import cmp_to_key
            a_cnt, b_cnt = bin(a).count('1'), bin(b).count('1')

            if a_cnt == b_cnt:
                return a - b
            
            return a_cnt - b_cnt

        sorted_arr = sorted(arr, key=cmp_to_key(sort_func))

        return sorted_arr