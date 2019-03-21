import re
from collections import Counter, defaultdict

class MostCommon:
    def mostCommonWord(self, paragraph: str, banned: 'List[str]') -> str:
        words = re.findall(r'\w+', paragraph.lower())
        return Counter(w for w in words if w not in banned).most_common(1)[0][0]

    def mostCommonWord2(self, paragraph: str, banned: 'List[str]') -> str:
        banned = set(banned)
        wordDict = defaultdict(int)
        words = paragraph.lower().translate(str.maketrans(string.punctuation, ' '*len(string.punctuation))).split()
        result = ''
        for word in words:
            if word not in banned:
                wordDict[word] += 1
                if wordDict[word] > wordDict[result]:
                    result = word
        return result