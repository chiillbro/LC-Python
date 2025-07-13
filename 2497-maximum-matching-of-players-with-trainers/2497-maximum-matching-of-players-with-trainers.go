func matchPlayersAndTrainers(players []int, trainers []int) int {
    sort.Slice(players, func (i,j int) bool { return players[i] < players[j] })
    sort.Slice(trainers, func (i,j int) bool { return trainers[i] < trainers[j] })

    j := 0
    matches := 0

    for _, ability := range players {
        for j < len(trainers) && ability > trainers[j] {
            j++
        }

        if j == len(trainers) {
            return matches
        }

        matches++
        j++
    }

    return matches
}