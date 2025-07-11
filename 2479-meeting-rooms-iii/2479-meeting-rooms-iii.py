class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        meetings.sort()
        
        times_used = [0] * (n)
        # room_availability_time = [0] * n

        # for start, end in meetings:
        #     min_room_availability_time = math.inf
        #     room_id = 0
        #     found_unused_room = False

        #     for i in range(n):
        #         if room_availability_time[i] <= start:
        #             found_unused_room = True
        #             room_availability_time[i] = end
        #             times_used[i] += 1
        #             break
        #         if room_availability_time[i] < min_room_availability_time:
        #             min_room_availability_time = room_availability_time[i]
        #             room_id = i
                    
        #     if not found_unused_room:
        #         room_availability_time[room_id] += end - start
        #         times_used[room_id] += 1



        # Using sorting and Priority Queue

        unused_rooms = list(range(n)); used_rooms = []

        for start, end in meetings:
            while used_rooms and used_rooms[0][0] <= start:
                _, room_id = heappop(used_rooms)
                heappush(unused_rooms, room_id)
            
            if unused_rooms:
                room_id = heappop(unused_rooms)
                heappush(used_rooms, [end, room_id])
            
            else:
                room_availability_time, room_id = heappop(used_rooms)
                heappush(
                    used_rooms,
                    [room_availability_time + end - start, room_id]
                )

            
            times_used[room_id] += 1

        max_times_used = max(times_used)
        return times_used.index(max_times_used)