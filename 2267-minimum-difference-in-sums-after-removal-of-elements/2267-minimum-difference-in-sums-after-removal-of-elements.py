class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        """
        nums: List[int], size = 3 * n elements (3 multiple elements -> 3, 6, 9, 12)

        returns:
            min diff of remaining two subseq groups after removing exactly n elements

        Let's think:
            how to optimally remove n elements, what is the deciding factor here
            - In order to make the min diff between two elements let's say 'a' and 'b' 
              (diff is 'a-b') we should be choosing 'a' as lesser as possible compared to 'b'
              or the very possible close number greater than 'b'

            - as we are dealing with two different sums here, I think prefix sums can be handy

        """ 
        N = len(nums)

        n = N // 3

        part1 = [0] * (n+1)

        total = sum(nums[:n])

        part1[0] = total

        ql = [-num for num in nums[:n]]
        heapify(ql)

        for i in range(n, 2 * n):
            total += nums[i]
            heappush(ql, -nums[i])
            total -= -heappop(ql)

            part1[i - (n-1)] = total

        part2 = sum(nums[2*n:])
        ans = part1[-1] - part2

        qr = nums[2*n:]
        heapify(qr)

        for i in range(2 * n - 1, n-1, -1):
            part2 += nums[i]
            heappush(qr, nums[i])

            part2 -= heappop(qr)

            ans = min(ans, part1[i-n] - part2)
    
        return ans