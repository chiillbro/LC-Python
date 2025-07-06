class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.data[key]

        if not pairs:
            return ""
        
        # timestamps = [pair[1] for pair in pairs]
        
        # idx = bisect_right(timestamps, timestamp)

        left, right = 0, len(pairs) - 1

        while left <= right:
            mid = (left + right) >> 1

            if pairs[mid][1] > timestamp:
                right = mid - 1
            else:
                left = mid + 1

        if right < 0:
            return ""
        
        return pairs[right][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)