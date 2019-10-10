class Sentence:
    def wordsTyping(self, sentence: 'List[str]', rows: int, cols: int) -> int:
        words = ' '.join(sentence) + ' '
        start, n = -1, len(words)
        memo = [0 for _ in range(n)]
        for i in range(n):
            if words[i] == ' ':
                start = i
            memo[i] = i - start - 1
        
        length = 0
        for _ in range(rows):
            length += cols
            length -= memo[length % n]
        return (length + 1) // n
