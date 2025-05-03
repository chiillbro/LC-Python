class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        res = self._canRotate(tops, bottoms, tops[0])

        if tops[0] != bottoms[0]:
            res = min(res, self._canRotate(tops, bottoms, bottoms[0]))
        
        return res if res != float('inf') else -1
        
    def _canRotate(self, tops: List[int], bottoms: List[int], target) -> int:
        top_mismatch = bottom_mismatch = 0

        for i in range(len(tops)):
            if tops[i] != target and bottoms[i] != target:
                return float("inf")
            
            if tops[i] != target:
                top_mismatch += 1
            
            if bottoms[i] != target:
                bottom_mismatch += 1
        
        return min(top_mismatch, bottom_mismatch)
