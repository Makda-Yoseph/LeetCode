class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        a=""
        b= ""
        for i in word1:
            a += i
        for i in word2:
            b += i
        if a == b:
            return True
        else:
            return False
        