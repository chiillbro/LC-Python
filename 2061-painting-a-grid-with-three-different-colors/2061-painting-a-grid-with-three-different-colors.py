class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10**9 + 7
        
        # Part 1: Figuring out valid ways to make ONE layer (one column)
        # dictionary to store all "good" patterns for a single layer ( a column)
        # key: mask (integer code for the pattern)
        # value: color (list of actual colors, e.g., [0, 1, 0])
        valid = dict()

        # Enumerate masks that meet the requirements within the range [0, 3^m)
        for mask in range(3**m):
            color = list()
            mm = mask
            for i in range(m):
                color.append(mm % 3)
                mm //= 3
            if any(color[i] == color[i + 1] for i in range(m - 1)):
                continue
            valid[mask] = color

        #Part 2: Figuring out which layers can sit on top of other layers
        # key: mast_top_layer
        # value: list of mask_layer_below that mask_top_layer can legally be placed on top of.
        adjacent = defaultdict(list)
        for mask1, color1 in valid.items():
            for mask2, color2 in valid.items():
                if not any(x == y for x, y in zip(color1, color2)):
                    adjacent[mask1].append(mask2)

        #Part 3: Building layer by layer (column by column) - This is Dynamic Programming
        # in iteration i, f[some_task] stores the number of ways to color the first i columns such that the i -th column has the pattern some_mask
        f = [int(mask in valid) for mask in range(3**m)]
        for i in range(1, n):
            # Temporary list to calculate f for the next iteration (i+1)
            g = [0] * (3**m)
            for mask2 in valid.keys():
                for mask1 in adjacent[mask2]:
                    g[mask2] += f[mask1]
                    if g[mask2] >= mod:
                        g[mask2] -= mod
            f = g

        return sum(f) % mod

# If m was large (like 20), 3^20 would be astronomically huge, and this approach wouldn't work. The small m is the key to why this "state compression" DP (where the "state" is the pattern of a whole column, compressed into an integer mask) is feasible