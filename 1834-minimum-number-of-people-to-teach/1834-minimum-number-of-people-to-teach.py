class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:

        # lang_to_users = defaultdict(set)

        # for user, langs in enumerate(languages):
        #     for lang in langs:
        #         lang_to_users[lang].add(user)

        cntcom = set()
        for u, v in friendships:
            cncom = set(languages[u-1])
            flag = False
            for lan in languages[v-1]:
                if lan in cncom:
                    flag = True
                    break
            
            if not flag:
                cntcom.add(u-1)
                cntcom.add(v-1)
        

        maxcnt = 0
        cnt = [0] * (n+1)

        for friend in cntcom:
            for lan in languages[friend]:
                cnt[lan] += 1
                maxcnt = max(maxcnt, cnt[lan])
        
        return len(cntcom) - maxcnt


        
