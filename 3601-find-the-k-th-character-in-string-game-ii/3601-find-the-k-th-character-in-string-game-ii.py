class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n = len(operations)
        # If there are no operations, the string is "a" -> k must be 1
        if n == 0:
            return 'a'
        
        # Precompute the lengths: L[0] = 1 (initial), L[i] = length after i operations
        L = [1] * (n + 1)
        for i in range(1, n + 1):
            L[i] = 2 * L[i - 1]
        
        shift = 0
        cur = k
        
        # Traverse operations in reverse order (from last to first)
        for i in range(n - 1, -1, -1):
            # If current position is in the second half
            if cur > L[i]:
                cur -= L[i]  # Adjust position to first half
                if operations[i] == 1:
                    shift = (shift + 1)  # Track transformations
        
        # Apply transformations mod 26 to base character 'a'
        return chr(ord('a') + (shift % 26))
    