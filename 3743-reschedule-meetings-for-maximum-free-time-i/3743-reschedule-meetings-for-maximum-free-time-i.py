class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        # Approach 1: Sliding Window

        n = len(startTime)

        # gaps = [0] * (n+1)

        gaps = []
        # gaps[0] = startTime[0] - 0
        gaps.append(startTime[0] - 0)

        for i in range(n-1):
            # gaps[i] = startTime[i] - endTime[i-1]
            gaps.append(startTime[i+1] - endTime[i])
        
        # gaps[n] = eventTime - endTime[n-1]
        gaps.append(eventTime - endTime[n-1])

        window_size = k + 1

        if len(gaps) <= window_size:
            return sum(gaps)
        
        current_window_gap_sum = sum(gaps[:window_size])
        max_free_time = current_window_gap_sum

        for i in range(1, len(gaps) - window_size + 1):
            current_window_gap_sum = current_window_gap_sum - gaps[i-1] + gaps[i + window_size - 1]

            max_free_time = max(current_window_gap_sum, max_free_time)
        
        return max_free_time