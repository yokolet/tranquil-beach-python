class ConfusingNumber:
    def confusingNumber(self, N: int) -> bool:
        mapping = {'0':'0', '1':'1', '8':'8', '9':'6', '6':'9'}
        orig, rot = str(N), ''
        for c in orig:
            if c not in mapping: return False
            rot = mapping[c] + rot
        return orig != rot
