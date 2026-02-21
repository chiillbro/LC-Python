class Solution:
    def is_prime(self, num):
        if num <= 1:
            return False
        
        
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        

        return True
    

    def count_set_bits(self, num):
        count = 0

        while num > 0:
            num = num & (num - 1)
            count += 1
    
        return count

    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left, right + 1):
            num = self.count_set_bits(i)

            if self.is_prime(num):
                count += 1

        
        return count