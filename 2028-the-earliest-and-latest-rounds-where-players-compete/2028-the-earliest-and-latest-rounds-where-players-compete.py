class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        # Try out every possible way and perform the checks

        # min_round, max_round = math.inf, -math.inf

        # players = list(range(1, n+1))


        # def backtrack(players, r):
        #     i, j = 0, len(players) - 1
        #     left_players = []
        #     right_players = []
        #     while i <= j:
        #         if players[i] == firstPlayer and players[j] == secondPlayer:
        #             min_round = min(r, min_round)
        #             max_round = max(r, max_round)
        #             left_players.append(players[i])
        #             right_players.append(players[j])
            
        #     for i in range(len(left_players)):
        #         cur_left = left_players[i]

        @cache
        def dp(n: int, f: int, s: int) -> (int, int):
            if f + s == n + 1:
                return 1, 1
            
            if f + s > n + 1:
                return dp(n, n + 1 - s, n + 1 - f)
            
            earliest, latest = math.inf, -math.inf

            n_half = (n + 1) >> 1

            if s <= n_half:
                for i in range(f):
                    for j in range(s-f):
                        x, y = dp(n_half, i+1, i+j+2)
                        earliest = min(earliest, x)
                        latest = max(latest, y)
            else:
                s_prime = n + 1 - s

                mid = (n - 2 * s_prime + 1) >> 1
                for i in range(f):
                    for j in range(s_prime - f):
                        x, y = dp(n_half, i + 1, i + j + mid + 2)
                        earliest = min(earliest, x)
                        latest = max(latest, y)
            
            return (earliest + 1, latest + 1)
    

        if firstPlayer > secondPlayer:
            firstPlayer, secondPlayer = secondPlayer, firstPlayer
        
        earliest, latest = dp(n, firstPlayer, secondPlayer)
        return [earliest, latest]