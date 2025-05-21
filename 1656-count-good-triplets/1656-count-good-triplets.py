class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        res = 0

        # for i in range(n):
        #     for j in range(i+1, n):
        #         ij = abs(arr[i] - arr[j])
        #         if ij > a:
        #             continue
                
        #         for k in range(j+1, n):
        #             jk = abs(arr[j] - arr[k])
        #             ik = abs(arr[i] - arr[k])

        #             if jk <= b and ik <= c:
        #                 res += 1

        # Somewhat Efficient - Cleverly using the constraints
        totals = [0] * 1001

        for j in range(n):
            for k in range(j+1, n):
                if abs(arr[j] - arr[k]) <= b:
                    lj, rj = arr[j] - a, arr[j] + a
                    lk, rk = arr[k] - c, arr[k] + c

                    l, r = max(0, lj, lk), min(1000, rj, rk)

                    if l <= r:
                        res += totals[r] if not l else totals[r] - totals[l-1]

            for i in range(arr[j], 1001):
                totals[i] += 1

        return res 
        
        return res
                