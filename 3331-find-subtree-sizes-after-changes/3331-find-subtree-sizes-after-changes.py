class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        parent_children_list = defaultdict(list)

        for i in range(1, n):
            parent_children_list[parent[i]].append(i)
        

        track_ancestors = defaultdict(list)
        new_parent = parent[:]

        def dfs(node):
            if s[node] in track_ancestors:
                new_parent[node] = track_ancestors[s[node]][-1]
            track_ancestors[s[node]].append(node)

            for child in parent_children_list[node]:
                dfs(child)
            track_ancestors[s[node]].pop()
            if not track_ancestors[s[node]]:
                del track_ancestors[s[node]]
        
        dfs(0)

        new_parent_children_list = defaultdict(list)

        for i in range(1, n):
            new_parent_children_list[new_parent[i]].append(i)
        
        ans = [0] * n
        def subtree_size(node):
            if node not in new_parent_children_list:
                ans[node] = 1
                return 1
            
            size = 1
            for child in new_parent_children_list[node]:
                size += subtree_size(child)
            
            ans[node] = size
            return size
        
        subtree_size(0)
        return ans