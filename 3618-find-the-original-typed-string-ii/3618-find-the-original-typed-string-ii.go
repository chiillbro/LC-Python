const MOD = 1000000007

func possibleStringCount(word string, k int) int {
    n := len(word)

    cnt := 1

    freq := []int{}

    for i := 1; i < n; i++ {
        if word[i] == word[i-1] {
            cnt++
        } else {
            freq = append(freq, cnt)
            cnt = 1
        }
    }
    
    freq = append(freq, cnt)

    res := 1

    for _, o := range freq {
        res = res * o % MOD
    }

    if len(freq) >= k {
        return res
    }
    f, pref :=make([]int, k), make([]int, k)

    f[0] = 1

    for i := range pref {
        pref[i] = 1
    }

    for i := 0; i < len(freq); i++ {
        f_new := make([]int, k)

        for j := 1; j < k; j++ {
            f_new[j] = pref[j-1]

            if idx := j - freq[i] - 1; idx >= 0 {
                f_new[j] = (f_new[j] - pref[idx] + MOD) % MOD
            }
        }

        pref_new := make([]int, k)

        pref_new[0] = f_new[0]

        for j := 1; j < k; j++ {
            pref_new[j] = (pref_new[j-1] + f_new[j]) % MOD
        }

        f, pref = f_new, pref_new
    }


    return (res - pref[k-1] + MOD) % MOD



    // canDelete := n - k
    // for i, _ := range word {
    //     j := i + 1

    //     for j < n && word[i] == word[j] {
    //         j += 1
    //     }

    //     if L := j - i; L > 1 {
    //         cur := L - 1
    //         res += min(cur, canDelete)
    //     }

    //     i = j
    // }

    // return res
}