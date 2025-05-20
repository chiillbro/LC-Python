class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)

        chains = defaultdict(int)

        for word in words:
            chains[word] = 1
            for i in range(len(word)):
                pred = word[:i] + word[i+1:]
                if pred in chains:
                    chains[word] = max(chains[word], chains[pred] + 1)
        
        return max(chains.values())