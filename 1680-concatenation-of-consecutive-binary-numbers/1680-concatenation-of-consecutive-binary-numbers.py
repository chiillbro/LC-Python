class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        binary_str = []
        for i in range(1, n+1):
            binary_frm = format(i, "b")
            binary_str.append(str(binary_frm))
        

        ans = "".join(binary_str)
        return int(ans, 2) % MOD
