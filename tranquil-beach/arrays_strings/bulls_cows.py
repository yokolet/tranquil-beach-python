from collections import defaultdict, Counter

class BullsCows:
    def getHint(self, secret: str, guess: str) -> str:
        b = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                b += 1
        sc = Counter(secret)
        gc = Counter(guess)
        cs = sc & gc
        return "{}A{}B".format(str(b), str(sum(cs.values()) - b))

    def getHint2(self, secret: str, guess: str) -> str:
        letters = defaultdict(int)
        for s in secret:
            letters[s] += 1
        b, cs = 0, []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                b += 1
                letters[secret[i]] -= 1
            elif guess[i] in secret:
                cs.append(guess[i])
        c = 0
        for s in cs:
            if letters[s] > 0:
                c += 1
                letters[s] -= 1
        return '{}A{}B'.format(str(b), str(c))
