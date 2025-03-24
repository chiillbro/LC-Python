class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        merged_meetings = self._mergeIntervals(sorted(meetings))

        res = 0
        end = 0
        # [[2, 8]]
        # [[1, 3], [5, 7], [9, 10]]

        for cur_s, cur_e in merged_meetings:
            if cur_s > end:
                res += cur_s - end - 1
            end = cur_e
        
        s = merged_meetings[-1][1]
        if s < days:
            res += days - s
        

        return res


    def _mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = [intervals[0]]

        for cur_s, cur_e in intervals[1:]:
            prev_s, prev_e = merged_intervals[-1]

            if cur_s <= prev_e:
                merged_intervals[-1] = [min(cur_s, prev_s), max(cur_e, prev_e)]
            else:
                merged_intervals.append([cur_s, cur_e])
        
        return merged_intervals