class Solution:
    def countLargestGroup(self, n: int) -> int:
        counter = Counter()
        _max_len = 1
        _max_no = 0
        for i in range(1, n + 1):
            _sum = 0
            while i > 0:
                _sum += (i % 10)
                i //= 10
            
            counter[_sum] += 1
            if _max_len == counter[_sum]:
                _max_no += 1
            elif _max_len < counter[_sum]:
                _max_len = counter[_sum]
                _max_no = 1
            # _max_len = max(counter[_sum], _max_len)
        
        # return sum(1 for v in counter.values() if v == _max_len)
        return _max_no