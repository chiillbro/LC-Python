class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0

        # Approach 1: Using enumeration (TC: O(N^3))
        # for i in range(len(arr) - 2):
        #     for j in range(i + 1, len(arr) - 1):
        #         for k in range(j + 1, len(arr)):
        #             x, y, z = abs(arr[i] - arr[j]), abs(arr[j] - arr[k]), abs(arr[i] - arr[k])
        #             if x <= a and y <= b and z <= c: res += 1
        
        # Approach 2: Using optimized enumeration (TC: O(N^2 + N*S)) where S is the upper limit - in this problem - it's 1000
        total = [0] * 1001

        for j in range(len(arr) - 1):
            for k in range(j + 1, len(arr)):
                if abs(arr[j] - arr[k]) <= b:
                    lj, rj = arr[j] - a, arr[j] + a
                    lk, rk = arr[k] - c, arr[k] + c
                    l = max(0, lj, lk)
                    r = min(1000, rj, rk)

                    if l <= r:
                        res += total[r] if not l else total[r] - total[l - 1]
            
            for k in range(arr[j], 1001):
                total[k] += 1
        
        return res