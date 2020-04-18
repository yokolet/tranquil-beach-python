from collections import defaultdict

class LongestStringChain:
    def longestStrChain(self, words: 'List[str]') -> int:
        def findPred(a):
            preds = set()
            for i in range(len(a)):
                tmp = a[:i]+a[i+1:]
                if tmp not in preds and tmp in w_dict[len(a)-1]:
                    preds.add(tmp)
            return preds
        
        w_dict = defaultdict(set)
        for w in words:
            w_dict[len(w)].add(w)
        max_len, memo = 1, defaultdict(lambda:1)
        for l in range(16, 1, -1):    # 1 <= words[i] <=16
            if l not in w_dict or l-1 not in w_dict: continue
            for w in w_dict[l]:
                preds = findPred(w)
                for p in preds:
                    memo[p] = max(memo[p], memo[w]+1)
                    max_len = max(max_len, memo[p])
        return max_len
