type Pair struct {
    value string
    timestamp int
}

type TimeMap struct {
    data map[string][]Pair
}


func Constructor() TimeMap {

    return TimeMap{
        data: make(map[string][]Pair),
    }
}


func (this *TimeMap) Set(key string, value string, timestamp int)  {
    this.data[key] = append(this.data[key], Pair{value, timestamp})
}


func (this *TimeMap) Get(key string, timestamp int) string {
    pairs := this.data[key]

    if len(pairs) == 0 {
        return ""
    }


    i := sort.Search(len(pairs), func (i int) bool {
        return pairs[i].timestamp > timestamp
    })

    if i == 0 {
        return ""
    }

    return pairs[i-1].value

    // left, right := 0, len(pairs) - 1

    // for left <= right {
    //     mid := (left + right) >> 1

    //     if pairs[mid].timestamp > timestamp {
    //         right = mid - 1
    //     } else {
    //         left = mid + 1
    //     }
    // }

    // if right < 0 || pairs[right].timestamp > timestamp {
    //     return ""
    // }

    // return pairs[right].value
}


/**
 * Your TimeMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Set(key,value,timestamp);
 * param_2 := obj.Get(key,timestamp);
 */