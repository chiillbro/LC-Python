class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        # Optimizations to the bottom approach

        # precompute every possible pattern

        L = len(beginWord)

        wildcards = defaultdict(list)
        for w in wordList:
            for i in range(L):
                pattern = w[:i] + '*' + w[i+1:]
                wildcards[pattern].append(w)
        
        front, back = {beginWord}, {endWord}
        visited = {beginWord, endWord}

        steps = 2

        while front and back:
            if len(front) > len(back):
                front, back = back, front

            next_front = set()

            for w in front:
                for i in range(L):
                    pattern = w[:i] + "*" + w[i+1:]

                    for word in wildcards[pattern]:
                        if word in back:
                            return steps
                        elif word not in visited:
                            visited.add(word)
                            next_front.add(word)
                    wildcards[pattern].clear()
            front = next_front
            steps += 1
    

        return 0
        # queue = deque([beginWord])
        # seen = set([beginWord])

        # steps = 1
        # while queue:
        #     for _ in range(len(queue)):
        #         cur_word = queue.popleft()

        #         if cur_word == endWord:
        #             return steps
                
        #         for i in range(len(cur_word)):
        #             for c in 'abcdefghijklmnopqrstuvwxyz':
        #                 new_word = cur_word[:i] + c + cur_word[i+1:]

        #                 if new_word in wordSet and new_word not in seen:
        #                     seen.add(new_word)
        #                     queue.append(new_word)
                    
            
        #     steps += 1
        
        # return 0