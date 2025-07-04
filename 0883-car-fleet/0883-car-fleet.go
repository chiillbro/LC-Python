func carFleet(target int, position []int, speed []int) int {
    // speed = distance / time

    // time = distance / speed

    // 10, 2 => 12 - 10 / 2 => 1
    // 8, 4 => 12 - 8 / 4 => 1

    // 5, 1 => 12 - 5 / 1 => 8
    // 3, 3, => 12 - 3 / 3 => 3

    // 0, 3, 5, 8, 10
    // 1, 3, 1, 4, 2

    // 12, 3, 7, 1, 1
    // lead = 1

    // 12, 3, 7, 1
    // lead = 1

    // 12, 3, 7
    // ans += 1
    // lead = 7

    // 12, 3
    // 12, 7

    // lead = 7
    // 12
    // ans +=1

    // terminates

    // return ans + 1

    n := len(position)

    cars := make([][]int, n)

    for i, v := range position {
        cars[i] = []int{v, speed[i]}
    }

    sort.Slice(cars, func (i, j int) bool { return cars[i][0] < cars[j][0]})

    times := make([]float64, n)

    for i, v := range cars {
        times[i] = float64(target - v[0]) / float64(v[1])
    }

    ans := 0

    for len(times) > 1 {
        lead := times[len(times) - 1]
        times = times[:len(times)-1]

        if lead < times[len(times)-1] {
            ans++
        } else {
            times[len(times)-1] = lead
        }
    }

    return ans + 1

}