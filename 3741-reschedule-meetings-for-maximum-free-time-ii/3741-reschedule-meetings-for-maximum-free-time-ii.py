class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:


        n = len(startTime)
        # gaps_left = defaultdict(int)

        # j = 0
        # for i in range(n):
        #     start = startTime[i]
        #     gaps_left[i] = start - j
        #     j = endTime[i]        

        # gaps_right = defaultdict(int)
        # j = eventTime

        # for i in range(n-1, -1, -1):
        #     end = endTime[i]

        #     gaps_right[i] = j - end
        #     j = startTime[i]
        
        gaps = []

        gaps.append(startTime[0] - 0)

        for i in range(n-1):
            gaps.append(startTime[i+1] - endTime[i])

        gaps.append(eventTime - endTime[n-1])

        print("gaps", gaps)

        k = len(gaps)

        gaps_left = [gaps[0]]

        for i in range(1, k):
            gaps_left.append(max(gaps_left[-1], gaps[i]))
        
        gaps_right = [0] * (k)

        gaps_right[-1] = gaps[-1]

        for i in range(k-2, -1, -1):
            gaps_right[i] = max(gaps_right[i+1], gaps[i])

        
        max_gap = max(gaps)

        print("gaps_left", gaps_left)

        print("gaps_right", gaps_right)

        for i in range(n):
            left = 0
            if i - 1 >= 0:
                left = gaps_left[i-1]
            
            right = 0

            if i + 2 < k:
                right = gaps_right[i+2]
            
            cur_gap = 0
            cur_dur = endTime[i] - startTime[i]
            if left >= cur_dur or right >= cur_dur:
                cur_gap = gaps[i] + gaps[i+1] + cur_dur
            
            else:
                cur_gap = gaps[i] + gaps[i+1]
            
            max_gap = max(max_gap, cur_gap)
        
        return max_gap


        return 0

            