import string, re

class ValidPalindrome:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        translator = str.maketrans('', '', string.punctuation + ' ')
        s = s.lower().translate(translator)
        return s == s[::-1]
    
    # looks regex is slow
    def isPalindrome3(self, s: 'str') -> 'bool':
        s = re.sub(r'\W+', '', s.lower())
        return s == s[::-1]

    def isPalindrome2(self, s):
        p = re.compile('[a-z0-9]')
        s = ''.join([c if p.match(c) else '' for c in s.lower()])
        return s == s[::-1]

