class Solution(object):
    def romanToInt(self, s):
        roman = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        l = len(s) - 1
        num = 0
        for i in range(len(s)):
            if i < l and roman[s[i]] < roman[s[i+1]]:
                num -= roman[s[i]]
            else:
                num += roman[s[i]]
        return num

