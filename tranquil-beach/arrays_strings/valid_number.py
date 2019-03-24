import re

class ValidNumber:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pat = re.compile(r'^\s*[+-]?(\d+(\.\d*)?|\.\d+)([Ee][+-]?\d+)?\s*$')
        return True if pat.match(s) else False

    def isNumber2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
        except ValueError:
            return False
        return True