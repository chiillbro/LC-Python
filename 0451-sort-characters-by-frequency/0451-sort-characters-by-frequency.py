class Solution:
    def frequencySort(self, s: str) -> str:
        # heap = []
        # freq = Counter(s)

        # for char, count in freq.items():
        #     heapq.heappush(heap, (-count, char))
        
        # res = ""

        # while heap:
        #     count, char = heapq.heappop(heap)
        #     res += (char * -count)

        # return res      

        freq = Counter(s) 

        ordered_dict = OrderedDict(sorted(freq.items(), key=lambda x : x[1], reverse=True)) 
        return ''.join([char * freq for char, freq in ordered_dict.items()])

