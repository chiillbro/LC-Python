class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        # res = []
        # found = False
        # layer = {beginWord : [[beginWord]]}

        # while layer and not found:
        #     new_layer = defaultdict(list)
        #     for word in layer:
        #         if word == endWord:
        #             found = True
        #             res.extend(layer[word])
                
        #         else:
        #             for i in range(len(word)):
        #                 for c in "abcdefghijklmnopqrstuvwxyz":
        #                     new_word = word[:i] + c + word[i+1:]
        #                     if new_word in wordList:
        #                         new_layer[new_word] += [path + [new_word] for path in layer[word]]
        #     wordList -= set(new_layer.keys())
        #     layer = new_layer
        
        # return res

        found = False
        predecessors = defaultdict(set)
        queue = deque([beginWord])
        visited = set([beginWord])

        while queue and not found:
            next_visited = set()
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordSet and new_word not in visited:
                            if new_word == endWord:
                                found = True
                            predecessors[new_word].add(word)
                            next_visited.add(new_word)
            queue.extend(next_visited)
            visited.update(next_visited)
            wordSet -= next_visited
        
        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for pred in predecessors[word]:
                dfs(pred, path + [pred])
            
        res = []
        if found:
            dfs(endWord, [endWord])
        return res