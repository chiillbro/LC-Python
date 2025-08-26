class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        greater_rect = greater_diag = 0

        for length, width in dimensions:
            diag = math.sqrt(length ** 2 + width ** 2)
            area = length * width
            if diag > greater_diag:
                greater_diag = diag
                greater_rect = area
            elif diag == greater_diag:
                greater_rect = max(area, greater_rect)

        return greater_rect 