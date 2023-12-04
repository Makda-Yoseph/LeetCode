class Solution(object):
    def freqAlphabets(self, s):
        alpha = ""
        i = len(s)-1
        while i >= 0:
            if s[i] != '#':
                f = chr(int(s[i]) +97 - 1)
                alpha += f
                i -= 1
            else:
                x = int(s[i-2:i])
                f = chr(x + 97 - 1)
                alpha += f
                i -= 3
        return alpha[::-1]