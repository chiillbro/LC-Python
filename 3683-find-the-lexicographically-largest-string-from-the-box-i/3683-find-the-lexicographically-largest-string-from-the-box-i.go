func answerString(word string, numFriends int) string {
    if numFriends == 1 {
        return word
    }
    n := len(word)

    var res string

    for i := 0; i < n; i++ {
        res = max(res, word[i: min(n - numFriends + i + 1, n)])
    }

    return res
}

// func max[T string | int](a, b T) T {
//         if a > b {
//             return a
//         }

//         return b
//}

// func min[T string | int](a, b T) T {
//         if b < a {
//             return b
//         }

//         return a
//}


// TC: O(n^2)
// SC: O(n)