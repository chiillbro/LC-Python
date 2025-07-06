type Pair struct {
    val string
    time int
}

type TimeMap struct {
    timeMap map[string][]*Pair
}


func Constructor() TimeMap {
    timeMap := make(map[string][]*Pair)

    return TimeMap{
        timeMap,
    }
}


func (this *TimeMap) Set(key string, value string, timestamp int)  {
    this.timeMap[key] = append(this.timeMap[key], &Pair{value, timestamp})
}


func (this *TimeMap) Get(key string, timestamp int) string {
    timeStamps := this.timeMap[key]

    if len(timeStamps) == 0 {
        return ""
    }

    left, right := 0, len(timeStamps) - 1

    for left <= right {
        mid := (left + right) >> 1

        if timeStamps[mid].time > timestamp {
            right = mid - 1
        } else {
            left = mid + 1
        }
    }

    if right < 0 || timeStamps[right].time > timestamp {
        return ""
    }

    return timeStamps[right].val
}


/**
 * Your TimeMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Set(key,value,timestamp);
 * param_2 := obj.Get(key,timestamp);
 */