class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occur = {c : i for i, c in enumerate(s)}

        max_e = start = 0
        partitions = []

        for i, c in enumerate(s):
            max_e = max(max_e, last_occur[c])

            if i == max_e:
                partitions.append(i - start + 1)
                start = i + 1
        
        return partitions