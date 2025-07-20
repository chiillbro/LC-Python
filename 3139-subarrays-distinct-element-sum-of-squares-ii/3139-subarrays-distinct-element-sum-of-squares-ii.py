# class Solution:
#     def sumCounts(self, nums: List[int]) -> int:
        

mod = 10**9 + 7

class Fenw:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, index, delta):
        i = index + 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i
            
    def get_prefix(self, index):
        if index < 0:
            return 0
        total = 0
        i = index + 1
        while i:
            total += self.tree[i]
            i -= i & -i
        return total

class RangeFenw:
    def __init__(self, n):
        self.n = n
        self.T1 = Fenw(n)
        self.T2 = Fenw(n)
        
    def range_update(self, l, r, val):
        self.T1.update(l, val)
        if r + 1 < self.n:
            self.T1.update(r + 1, -val)
        self.T2.update(l, val * (l - 1))
        if r + 1 < self.n:
            self.T2.update(r + 1, -val * r)
            
    def prefix_sum(self, index):
        if index < 0:
            return 0
        a = self.T1.get_prefix(index) * index
        b = self.T2.get_prefix(index)
        return a - b
        
    def range_query(self, l, r):
        if l > r:
            return 0
        return self.prefix_sum(r) - self.prefix_sum(l - 1)

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        BIT = RangeFenw(n)
        last_occurrence = {}
        total_ans = 0
        F_prev = 0
        
        for j in range(n):
            num = nums[j]
            k = last_occurrence.get(num, -1)
            
            if k + 1 <= j - 1:
                seg_sum = BIT.range_query(k + 1, j - 1)
            else:
                seg_sum = 0
                
            F_j = F_prev + (j - k) + 2 * seg_sum
            total_ans = (total_ans + F_j) % mod
            
            if k + 1 <= j - 1:
                BIT.range_update(k + 1, j - 1, 1)
            BIT.range_update(j, j, 1)
            
            last_occurrence[num] = j
            F_prev = F_j
            
        return total_ans % mod