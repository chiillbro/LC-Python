class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        start = res = 0

        freq = defaultdict(int)

        for end in range(n):
            freq[fruits[end]] += 1
            while len(freq) > 2:
                freq[fruits[start]] -= 1
                if not freq[fruits[start]]:
                    freq.pop(fruits[start])
                start += 1
            
            res = max(res, end - start + 1)


        # Let's use hashset

        # track = set()

        # for end in range(n):
        #     while len(track) > 2:
        #         track.remove(fruits[start])
        #         start += 1

        #     track.add(fruits[end])

        #     res = max(res, end - start + 1)

        # nope, cann't use hashset, because accounting the freq of every fruit cannot be handled by hashset, for example consider this example, [3,3,3,1,2,1,1,2,3,3,4], once the end pointer reaches the type 2 fruit (at index = 4), then the len(set) becomes 3 and it should shrink the window, so it will remove the total type 3 fruit(start = 0) instance from the set, but if we observe, start = 1, 2 are also type 3 fruit, so hashset fails here
        
        return res
