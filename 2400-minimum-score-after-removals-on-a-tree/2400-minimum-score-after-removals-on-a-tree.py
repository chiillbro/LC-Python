class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        total = 0

        for val in nums:
            total ^= val
        
        res = math.inf

        def calculate(part1, part2, part3):
            return max(part1, part2, part3) - min(part1, part2, part3)

        def dfs2(node, parent, val, anc):
            cur_val = nums[node]
            for neigh in adj[node]:
                if neigh != parent:
                    cur_val ^= dfs2(neigh, node, val, anc)
            
            if parent == anc:
                return cur_val
            
            nonlocal res
            res = min(res, calculate(val, cur_val, total ^ val ^ cur_val))

            return cur_val
        
        def dfs(node, parent):
            cur_val = nums[node]

            for neigh in adj[node]:
                if neigh != parent:
                    cur_val ^= dfs(neigh, node)
            
            for neigh in adj[node]:
                if neigh == parent:
                    dfs2(neigh, node, cur_val, node)
            
            return cur_val
        
        dfs(0, -1)
        return res