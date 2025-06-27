class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)

        for u, v in prerequisites:
            adj_list[v].append(u)
        

        in_degree = [0] * numCourses

        for prereq in range(numCourses):
            for crs in adj_list[prereq]:
                in_degree[crs] += 1
        
        queue = deque(i for i in range(numCourses) if in_degree[i] == 0)

        topo = []
        while queue:
            cur = queue.popleft()
            topo.append(cur)

            for crs in adj_list[cur]:
                in_degree[crs] -= 1

                if in_degree[crs] == 0:
                    queue.append(crs)
        

        return topo if len(topo) == numCourses else []
