class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        # adj_list = defaultdict(list)
        # wordList.add(beginWord)
        # for word in wordList:
        #     for j in range(len(word)):
        #         pattern = word[:j] + "*" + word[j+1:]
        #         adj_list[pattern].append(word)

        visited = set([beginWord])
        queue = deque([beginWord])
        steps = 1

        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return steps

                for j in range(len(word)):
                    # pattern = word[:j] + "*" + word[j+1:]
                    # for nei in adj_list[pattern]:
                    #     if nei not in visited:
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:j] + c + word[j+1:]
                        if new_word in wordList and new_word not in visited:
                            visited.add(new_word)
                            queue.append(new_word)
            steps += 1
        
        return 0