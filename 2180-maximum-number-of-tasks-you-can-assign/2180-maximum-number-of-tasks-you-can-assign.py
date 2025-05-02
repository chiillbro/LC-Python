from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        m, n = len(workers), len(tasks)

        workers.sort()
        tasks.sort()


        def check(k: int) -> bool:
            p = pills

            # If k is 0, it's always possible. can handle this in the binary search boundary or here.
            if k == 0: return True

            # Consider the k strongest workers. Create a SortedList from them.
            # workers[m-k:] slices the last k elements (strongest ones).
            ws = SortedList(workers[m - k:])

            # Iterate through the k easiest tasks, from hardest (k-1) to easiest (0)
            for i in range(k - 1, -1, -1):
                current_task_strength = tasks[i]
                
                 # Check if the strongest available worker can do it WITHOUT a pill
                # ws[-1] gives the largest element in SortedList ws.
                if ws[-1] >= current_task_strength:
                    ws.pop()    # Remove the strongest worker (index -1 or len(ws)-1)
                # Else, we MUST use a pill (if possible)
                else:
                    if p == 0:
                        return False # No pills, cannot complete this task

                    # Find the index of the WEAKEST worker who CAN do it WITH a pill
                    # We need worker_strength >= current_task_strength - strength
                    # bisect_left finds the insertion point for this value, which corresponds
                    # to the index of the first element >= the value.
                    required_strength_without_pill = current_task_strength - strength

                    idx = ws.bisect_left(required_strength_without_pill)

                    # Check if such a worker was found
                    # If idx == len(ws), it means all workers in ws are weaker than required.
                    if idx == len(ws):
                        return False

                    # If found, use a pill and remove that weakest suitable worker
                    p -= 1 # Consume a pill
                    ws.pop(idx)
            
            # If the loop completes, we managed to assign all k tasks
            return True 


        # Binary search for the answer k
        low, high = 0, min(m, n)    # Range of possible number of tasks
        ans = 0

        while low <= high:
            mid = (high + low) >> 1

            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
        