class Solution(object):
    def isPalindrome(self, x):
        m = str(x)
        if m != m[::-1]:
            return False
        return True
        

        