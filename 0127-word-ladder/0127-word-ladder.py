class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0
        
        queue = deque([beginWord])
        seen = set([beginWord])

        steps = 1
        while queue:
            for _ in range(len(queue)):
                cur_word = queue.popleft()

                if cur_word == endWord:
                    return steps
                
                for i in range(len(cur_word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = cur_word[:i] + c + cur_word[i+1:]

                        if new_word in wordSet and new_word not in seen:
                            seen.add(new_word)
                            queue.append(new_word)
                    
            
            steps += 1
        
        return 0