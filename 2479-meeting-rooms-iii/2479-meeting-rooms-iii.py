class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        meetings.sort()
        
        times_used = [0] * (n)
        room_availability_time = [0] * n

        for start, end in meetings:
            min_room_availability_time = math.inf
            room_id = 0
            found_unused_room = False

            for i in range(n):
                if room_availability_time[i] <= start:
                    found_unused_room = True
                    room_availability_time[i] = end
                    times_used[i] += 1
                    break
                if room_availability_time[i] < min_room_availability_time:
                    min_room_availability_time = room_availability_time[i]
                    room_id = i
                    
            if not found_unused_room:
                room_availability_time[room_id] += end - start
                times_used[room_id] += 1

        max_times_used = max(times_used)

        return times_used.index(max_times_used)

        # time = meetings[0][0]

        # pq = []
        
        # rooms_used = 0

        # while True:
        #     heappush(pq, ())