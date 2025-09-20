class Router:

    def __init__(self, memoryLimit: int):
        self.size = memoryLimit
        self.queue = deque()

        self.packets = set()

        self.destination_map = defaultdict(lambda: {"timestamps": [], "start": 0})

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packets:
            return False
        
        if self.size == len(self.queue):
            src, dest, ts = self.queue.popleft()
            self.packets.remove((src, dest, ts))

            entry = self.destination_map[dest]
            entry["start"] += 1
        
        self.queue.append((packet))
        self.packets.add((packet))
        self.destination_map[destination]["timestamps"].append(timestamp)

        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        
        src, dest, ts = self.queue.popleft()
        self.packets.remove((src, dest, ts))

        entry = self.destination_map[dest]
        entry["start"] += 1

        return [src, dest, ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.destination_map:
            return 0
        
        timestamps = self.destination_map[destination]["timestamps"]
        start = self.destination_map[destination]["start"]

        left = bisect_left(timestamps, startTime, lo=start)
        right = bisect_right(timestamps, endTime, lo=start)

        return right - left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)