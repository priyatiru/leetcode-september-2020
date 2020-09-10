class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        guess = list(guess)
        secret = list(secret)
        counter = collections.Counter(secret)
        a_counts, b_counts = 0, 0
        
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                counter[secret[i]] -= 1
                guess[i] = 'A'
                secret[i] = 'A'
                a_counts += 1
                
        
        for i in range(len(guess)):
            if guess[i] != 'A' and counter[guess[i]] > 0:
                counter[guess[i]] -= 1
                guess[i] = 'B'
                b_counts += 1
                
        return str(a_counts) + 'A'+ str(b_counts) + 'B'
        