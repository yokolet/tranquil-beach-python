class StringTransformation:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2: return True
        if len(set(str2)) == 26: return False
        pair = {}
        for c1, c2 in zip(str1, str2):
            if c1 not in pair:
                pair[c1] = c2
            elif pair[c1] != c2:
                return False
        return True
