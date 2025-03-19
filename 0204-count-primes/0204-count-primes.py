class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        
        return len(self.sieveoferatosthenes(n))
    
    def sieveoferatosthenes(self, N):
        primes = [True] * N

        p = 2
        while p * p < N:
            if primes[p]:
                for i in range(p*p, N, p):
                    primes[i] = False
            
            p += 1

        # for i in range(2, N):
        #     for j in range(2, int(math.sqrt(i)) + 1):
        #         if j != i and i % j == 0:
        #             primes[i] = False
        #             break
        
        return [i for i in range(2, N) if primes[i]]