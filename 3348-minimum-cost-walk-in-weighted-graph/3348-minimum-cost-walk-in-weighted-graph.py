class UnionFind:
    def __init__(self, n : int):
        self.parent = list(range(n))
        self.size = [0] * n
    
    def find(self, a : int) -> int:
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        
        return self.parent[a]
    
    def union(self, a : int, b : int):
        pa = self.find(a)
        pb = self.find(b)
        if pa != pb:
            if self.size[pa] < self.size[pb]:
                self.parent[pa] = pb
                self.size[pb] += self.size[pa]
            else:
                self.parent[pb] = pa
                self.size[pa] += self.size[pb]

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # adj_matrix = defaultdict(list)
        # weights_map = defaultdict(int)
        # Bits = 18

        # uf_by_bit = [UnionFind(n) for _ in range(Bits)]

        uf = UnionFind(n)

        for u, v, w in edges:
            # for bit in range(Bits):
            #     if (w & (1 << bit)) == 0:
            #         uf_by_bit[bit].union(u, v)
            uf.union(u,v)
            # adj_matrix[u].append(v)
            # adj_matrix[v].append(u)
            # weights_map[(u, v)] == weights_map[(v, u)] = w
        
        # def findMinCost(start, end):
        #     pass

        component_cost = {}

        for u, v, w in edges:
            root = uf.find(u)
            if root not in component_cost:
                component_cost[root] = w
            else:
                component_cost[root] &= w
            
        res = []
        for start, end in query:
            # if not start in adj_matrix or not end in adj_matrix:
            #     res.append(-1)
            
            # res.append(findMinCost(start, end))
            # cost = 0
            # for bit in range(Bits): 
            #     if uf_by_bit[bit].find(start) != uf_by_bit[bit].find(end):
            #         cost |= (1 << bit)
            r1, r2 = uf.find(start), uf.find(end)
            if r1 != r2:
                res.append(-1)
            else:
                res.append(component_cost[r1])
            
            # res.append(cost)
    
        return res