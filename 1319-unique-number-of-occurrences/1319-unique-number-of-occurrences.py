class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_map = defaultdict(int)

        for num in arr:
            count_map[num] += 1
        

        return len(count_map.values()) == len(set(count_map.values()))