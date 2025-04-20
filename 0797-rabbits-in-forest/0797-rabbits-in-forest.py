class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = defaultdict(list)
        
        # ans = 0
        # for i, ans in enumerate(answers):
        #     same_col_rab = ans + 1
        #     if len(counter[same_col_rab]) == 0:
        #         ans += same_col_rab
        #         counter[same_col_rab].append([i])
        #     elif len(counter[same_col_rab][-1]) <  same_col_rab:
        #         counter[same_col_rab][-1].append(i)
        #     else:
        #         counter[same_col_rab].append([i])
        #         ans += same_col_rab
        
        # return ans

        counter = Counter(answers)

        res = 0

        for k, v in counter.items():
            group_size = k + 1
            groups = math.ceil(v / group_size)
            res += groups * group_size
        return res
