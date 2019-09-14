class LicenseKey:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = ''.join(S.upper().split('-'))[::-1]
        result = []
        for i in range(0, len(S), K):
            result.append(S[i:i+K])
        return '-'.join(result)[::-1]

    def licenseKeyFormatting2(self, S: str, K: int) -> str:
        result = ''
        count = K
        for i in range(len(S)-1, -1, -1):
            if S[i] != '-':
                result = S[i].upper() + result
                count -= 1
            if count == 0:
                result = '-' + result
                count = K
        return result if len(result) == 0 or result[0] != '-' else result[1:]
