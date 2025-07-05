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


    queue := make([]string, 0, n+1)

    visited[beginWord] = struct{}{} 

    queue = append(queue, beginWord)

    steps := 1
    for len(queue) > 0 {
        size := len(queue)

        for i := 0; i < size; i++ {
            curWord := queue[0]

            if curWord == endWord {
                return steps
            }
            queue = queue[1:]
            for i, _ := range curWord {
                fmt.Println("curWord", curWord)
                for _, chr := range "abcdefghijklmnopqrstuvwxyz" {
                    var b strings.Builder

                    b.WriteString(curWord[:i])
                    b.WriteRune(chr)
                    b.WriteString(curWord[i+1:])

                    newW := b.String()


                    fmt.Println("newW", newW)

                    _, exists := wordMap[newW]
                    _, exists2 := visited[newW]


                    // if wordMap[newW] == struct{}{} && visited[newW] != struct{}{} {
                    if exists && !exists2 {
                        visited[newW] = struct{}{}
                        queue = append(queue, newW)
                    }
                }
            }
        }
        steps++
    }

    return 0
}