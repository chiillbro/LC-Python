class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        # def sort_func(a, b):
        #     if a[0] > b[0]:
        #         return -1
        #     if a[0] < b[0]:
        #         return 1
        #     else:
        #         if b[0] > b[1]:
        #             return 1
        #         else:
        #             return -1

        envelopes.sort(key=lambda x:(x[0], -x[1]))

        LIS = []; size = 0

        for _, h in envelopes:
            if not LIS or h > LIS[-1]:
                LIS.append(h); size += 1
            else:
                insert_idx = bisect_left(LIS, h)
                # l, r = 0, size
                # while l <= r:
                #     m = (l + r) >> 1
                #     if LIS[m] < h:
                #         l = m + 1
                #     else:
                #         r = m - 1
                # LIS[l] = h
                LIS[insert_idx] = h
        return size
