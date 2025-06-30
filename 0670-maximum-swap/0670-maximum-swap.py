class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))

        track = {int(num): i for i, num in enumerate(num_str)}

        for i in range(len(num_str)):
            cur = num_str[i]
            for j in range(9, int(cur), -1):
                if j in track and track[j] > i:
                    swap_idx = track[j]
                    num_str[i], num_str[swap_idx] = num_str[swap_idx], num_str[i]

                    return int(''.join(num_str))
        
        return num






        