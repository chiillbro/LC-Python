class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        y_intervals, x_intervals = [], []

        for startx, starty, endx, endy in rectangles:
            y_intervals.append([starty, endy])
            x_intervals.append([startx, endx])
        

        y_intervals.sort(); x_intervals.sort()

        return max(self._mergeIntervals(x_intervals)[1], self._mergeIntervals(y_intervals)[1]) >= 3
    
    def _mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = [intervals[0]]

        for cur_s, cur_e in intervals[1:]:
            prev_s, prev_e = merged[-1]

            if cur_s < prev_e:
                merged[-1] = [min(cur_s, prev_s), max(cur_e, prev_e)]
            else:
                merged.append([cur_s, cur_e])
        
        return merged, len(merged)