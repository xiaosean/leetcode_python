class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        table = {}
        A = 0
        B = 0
        for i in range(len(secret)):
            table[secret[i]] = table.get(secret[i], 0) + 1
            if guess[i] in table:
                if guess[i] == secret[i]:
                    A += 1
                    table[secret[i]] -= 1
            
        for i, num in enumerate(secret):
            if guess[i] != num and table.get(guess[i], 0):
                table[guess[i]] -= 1
                B += 1
        return f"{A}A{B}B"