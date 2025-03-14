class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0

        for i,v in enumerate(guess):
            if v == secret[i]:
                bulls += 1
        
        secret_count = Counter(secret)
        guess_count = Counter(guess)

        cows = sum(min(secret_count[d], guess_count[d]) for d in secret_count) - bulls

        return f"{bulls}A{cows}B"