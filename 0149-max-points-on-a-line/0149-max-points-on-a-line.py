class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        if n < 3:
            return n
        
        m = 1

        for i in range(n):
            if n - i + 1 <= m:
                break
            
            slopes = defaultdict(int)
            dup = 1 # accounts for duplicate points

            local_max = 0

            slopes_get = slopes.get
            slopes_set = slopes.__setitem__

            x1, y1 = points[i]

            for j in range(i+1, n):
                dx = points[j][0] - x1
                dy = points[j][1] - y1


                if dx == 0 and dy == 0:
                    dup += 1
                    continue
                
                # normalize signs + reduce dy/dx
                from math import gcd
                g = gcd(dx, dy)

                dx //= g
                dy //= g

                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0 and dy < 0:
                    dy = -dy
                

                key = (dx, dy)

                cnt = slopes_get(key, 0) + 1
                slopes_set(key, cnt)

                local_max = max(local_max, cnt)

                if local_max + dup + n - j - 1 <= m:
                    break
            
            m = max(local_max + dup, m)
        
        return m
