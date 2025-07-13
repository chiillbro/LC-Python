func findContentChildren(g []int, s []int) int {
    sort.Ints(g); sort.Ints(s)

    j, content := 0, 0

    for _, gF := range g {
        for j < len(s) && s[j] < gF {
            j++
        }

        if j == len(s) {
            return content
        }

        content++
        j++
    }

    return content
}