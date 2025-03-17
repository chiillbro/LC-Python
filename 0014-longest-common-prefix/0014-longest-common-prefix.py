class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
    def findLcp(self, total_words):
        node = self.root

        lcp = []

        while node and len(node.children) == 1:
            char = next(iter(node.children))
            if node.children[char].count == total_words:
                lcp.append(char)
                node = node.children[char]
            else:
                break
        return ''.join(lcp)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        N = len(strs)
        # trie = Trie()
        # for word in strs:
        #     trie.insert(word)
        
        # return trie.findLcp(N)
        pref = strs[0]

        for s in strs[1:]:
            while not s.startswith(pref):
                pref = pref[:-1]
                if not pref:
                    return ""

        return pref
        
