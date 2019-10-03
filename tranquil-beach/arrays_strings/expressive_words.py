class ExpressiveWords:
    def expressiveWords(self, S: str, words: 'List[str]') -> int:
        def findGroup(w):
            prev, chars, counts = '', [], []
            for i in range(len(w)):
                if prev == w[i]:
                    counts[-1] += 1
                else:
                    chars.append(w[i])
                    counts.append(1)
                prev = w[i]
            return chars, counts
        
        chars, counts = findGroup(S)
        result = 0
        for w in words:
            w_chars, w_counts = findGroup(w)
            if chars != w_chars: continue
            result += all(cnt >= max(w_cnt, 3) or cnt == w_cnt
                       for cnt, w_cnt in zip(counts, w_counts))
        return result

    def expressiveWords1(self, S: str, words: 'List[str]') -> int:
        def findGroup(w):
            prev, group = '', []
            for i in range(len(w)):
                if prev == w[i]:
                    group[-1][1] += 1
                else:
                    group.append([w[i], 1])
                prev = w[i]
            return group

        counts = findGroup(S)
        result = 0
        for w in words:
            w_counts = findGroup(w)
            if len(counts) != len(w_counts): continue
            found = True
            for i in range(len(counts)):
                if counts[i][0] != w_counts[i][0]:
                    found = False
                    break
                if counts[i][1] == w_counts[i][1] or \
                    counts[i][1] >= max(w_counts[i][1], 3):
                    continue
                else:
                    found = False
                    break
            if found:
                result += 1

        return result
