func groupAnagrams(strs []string) [][]string {
    groups := make(map[string][]string)

    for _, s := range strs {
        b := []byte(s)

        sort.Slice(b, func (i, j int) bool { return b[i] < b[j] })
        key := string(b)

        groups[key] = append(groups[key], s)
    }


    res := make([][]string, 0, len(groups))

    for _, group := range groups {
        res = append(res, group)
    }

    return res
}