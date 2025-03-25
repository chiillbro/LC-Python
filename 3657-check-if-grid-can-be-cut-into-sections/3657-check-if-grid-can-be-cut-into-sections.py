class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # y_intervals, x_intervals = [], []

        # for startx, starty, endx, endy in rectangles:
        #     y_intervals.append([starty, endy])
        #     x_intervals.append([startx, endx])
        

        # y_intervals.sort(); x_intervals.sort()

        return max(self._mergeIntervals(rectangles, 0), self._mergeIntervals(rectangles, 1)) >= 2
    
    def _mergeIntervals(self, rectangles: List[List[int]], coor: int) -> List[List[int]]:
        cuts = 0
        rectangles.sort(key=lambda rect: rect[coor])
        prev_e = rectangles[0][coor + 2]

        for interval in rectangles[1:]:
            if prev_e <= interval[coor]:
                cuts += 1
            
            prev_e = max(prev_e, interval[coor + 2])
        
        return cuts