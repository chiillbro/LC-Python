class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        res = meetings[0][0] - 1
        prev_start, prev_end = meetings[0][0], meetings[0][1]
        # [[2, 8]]
        # [[1, 3], [5, 7], [9, 10]]

        for cur_s, cur_e in meetings[1:]:
            if cur_s > prev_end + 1:
                res += cur_s - prev_end - 1
            prev_end = max(cur_e, prev_end)
        
        if prev_end < days:
            res += days - prev_end
        
        return res


    # def _mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
    #     merged_intervals = [intervals[0]]

    #     for cur_s, cur_e in intervals[1:]:
    #         prev_s, prev_e = merged_intervals[-1]

    #         if cur_s <= prev_e:
    #             merged_intervals[-1] = [min(cur_s, prev_s), max(cur_e, prev_e)]
    #         else:
    #             merged_intervals.append([cur_s, cur_e])
        
    #     return merged_intervals