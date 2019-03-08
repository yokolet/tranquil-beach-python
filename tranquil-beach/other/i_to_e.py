class IntegerToEnglish:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        under19 = [
            'One', 'Two', 'Three', 'Four',
            'Five', 'Six', 'Seven', 'Eight', 'Nine', 
            'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
            'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
            ]
        tens = [
            'Twenty', 'Thirty', 'Forty',
            'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'
            ]
        orders = [
             'Thousand', 'Million', 'Billion'
            ]
        def toEnglish(num):
            if num < 20: return under19[num-1:num]
            if num < 100: return [tens[num // 10 - 2]] + toEnglish(num % 10)
            if num < 1000: return [under19[num // 100 - 1]] + ['Hundred'] + toEnglish(num % 100)
            for i, order in enumerate(orders, 1):
                if num < 1000**(i+1): return toEnglish(num // 1000**i) + [order] + toEnglish(num % 1000**i)
        
        return ' '.join(toEnglish(num)) or 'Zero'