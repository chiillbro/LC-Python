func ladderLength(beginWord string, endWord string, wordList []string) int {

    n := len(wordList)
    wordMap := make(map[string]struct{}, n)

    for _, word := range wordList {
        wordMap[word] = struct{}{}
    }


    if _, exists := wordMap[endWord]; !exists {
        return 0
    }
    // if wordMap[endWord] != struct{}{} {
    //     return 0
    // }

    visited := make(map[string]struct{}, n+1)


    // queue := make([]string, 0, n+1)
    queue := []string{beginWord}

    visited[beginWord] = struct{}{}

    // queue = append(queue, beginWord)

    steps := 1
    for len(queue) > 0 {
        size := len(queue)

        for i := 0; i < size; i++ {
            curWord := queue[0]

            if curWord == endWord {
                return steps
            }
            queue = queue[1:]
            b := []byte(curWord)
            for pos := 0; pos < len(b); pos++ {
                original := b[pos]

                // for _, chr := range "abcdefghijklmnopqrstuvwxyz" {
                for c := byte('a'); c <= byte('z'); c++ {
                    if c == original {
                        continue
                    }
                    // var b strings.Builder

                    // b.WriteString(curWord[:i])
                    // b.WriteRune(chr)
                    // b.WriteString(curWord[i+1:])

                    // newW := b.String()
                    
                    b[pos] = c
                    next := string(b)
                    _, exists := wordMap[next]
                    _, exists2 := visited[next]


                    // if wordMap[newW] == struct{}{} && visited[newW] != struct{}{} {
                    if exists && !exists2 {
                        visited[next] = struct{}{}
                        queue = append(queue, next)
                    }
                }

                b[pos] = original
            }
        }
        steps++
    }

    return 0
}