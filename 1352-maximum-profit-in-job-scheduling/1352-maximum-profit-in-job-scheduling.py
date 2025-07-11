class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)

        jobs = []

        for i in range(n):
            jobs.append((startTime[i], endTime[i], profit[i]))
        
        jobs.sort()

        starts = [start for start, _, _ in jobs]

        nxt = [0] * n

        for i in range(n):
            nxt[i] = bisect_left(starts, jobs[i][1])
        
        memo = {}
        def dfs(cur_idx):
            if cur_idx >= n:
                return 0

            if cur_idx in memo:
                return memo[cur_idx]
            
            perform = jobs[cur_idx][2] + dfs(nxt[cur_idx])

            skip = dfs(cur_idx + 1)

            memo[cur_idx] = max(perform, skip)

            return memo[cur_idx]
        
        return dfs(0)