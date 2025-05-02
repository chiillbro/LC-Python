from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        m, n = len(workers), len(tasks)

        workers.sort()
        tasks.sort()


        def check(k: int) -> bool:
            p = pills

            if k == 0: return True

            ws = SortedList(workers[m - k:])

            for i in range(k - 1, -1, -1):
                current_task_strength = tasks[i]

                if ws[-1] >= current_task_strength:
                    ws.pop()
                
                else:
                    if p == 0:
                        return False

                    required_strength_without_pill = current_task_strength - strength

                    idx = ws.bisect_left(required_strength_without_pill)

                    if idx == len(ws):
                        return False

                    p -= 1
                    ws.pop(idx)

            return True 


        low, high = 0, min(m, n)
        ans = 0

        while low <= high:
            mid = (high + low) >> 1

            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
        