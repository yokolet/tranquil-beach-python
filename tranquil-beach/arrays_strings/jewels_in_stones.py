class JewelsInStones:
    def numJewelsInStones2(self, J: str, S: str) -> int:
        count = 0
        for s in S:
            if s in J: count += 1
        return count

    def numJewelsInStones(self, J: str, S: str) -> int:
        return len([s for s in S if s in J])