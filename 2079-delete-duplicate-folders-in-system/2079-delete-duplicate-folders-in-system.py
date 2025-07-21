class Trie:
    def __init__(self):
        self.str_repr = ""
        self.children = defaultdict(Trie)



class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Trie()

        # build the structure

        for path in paths:
            cur = root
            for node in path:
                if node not in cur.children:
                    cur.children[node] = Trie()
                
                cur = cur.children[node]
        
        # format string repres

        freq = defaultdict(int)
        def formatPaths(node: Trie):
            if not node.children:
                return
            
            cur = []
            for folder, child in node.children.items():
                formatPaths(child)
                cur.append(folder + "(" + child.str_repr + ")")
            
            print("before sorting", cur)
            cur.sort()
            print("after sorting", cur)

            node.str_repr = ''.join(cur)
            freq[node.str_repr] += 1
        
        formatPaths(root)

        print(root.children, root.str_repr)
        
        ans, path = [], []
        def resolve(node: Trie):
            if freq[node.str_repr] > 1:
                return
            
            if path:
                ans.append(path[:])
            
            for folder, child in node.children.items():
                path.append(folder)
                resolve(child)
                path.pop()
        
        resolve(root)
            
        
        return ans



