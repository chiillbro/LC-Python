class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

        self.size = [1] * n
        
        # self.comps = n

    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x, y):
        xRoot, yRoot = self.find(x), self.find(y)

        if xRoot == yRoot:
            return
        
        if self.size[xRoot] < self.size[yRoot]:
            xRoot, yRoot = yRoot, xRoot
        
        self.parent[yRoot] = xRoot
        self.size[xRoot] += self.size[yRoot]
        # self.comps -= 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        mail_map = defaultdict(int)

        uf = DSU(n)

        for i in range(n):
            if not accounts[i]:
                cotinue
            
            for mail in accounts[i][1:]:
                if mail in mail_map:
                    uf.union(i, mail_map[mail])
                else:
                    mail_map[mail] = i
        
        merged_mails = [[] for _ in range(n)]

        for mail, parent in mail_map.items():
            ultimate_par = uf.find(parent)
            if ultimate_par == parent:
                merged_mails[parent].append(mail)
            else:
                merged_mails[ultimate_par].append(mail)
        
        ans = []
        for i, mails in enumerate(merged_mails):
            if mails:
                ans.append([accounts[i][0]] + sorted(mails))
        
        return ans

            