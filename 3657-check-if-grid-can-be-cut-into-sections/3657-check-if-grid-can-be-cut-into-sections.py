class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        y_intervals, x_intervals = [], []

        for startx, starty, endx, endy in rectangles:
            y_intervals.append([starty, endy])
            x_intervals.append([startx, endx])
        

        y_intervals.sort(); x_intervals.sort()

        return max(self._mergeIntervals(x_intervals), self._mergeIntervals(y_intervals)) >= 2
    
    def _mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        cuts = 0
        prev_e = intervals[0][1]

        for cur_s, cur_e in intervals[1:]:
            if prev_e <= cur_s:
                cuts += 1
            
            prev_e = max(prev_e, cur_e)
        
        return cuts