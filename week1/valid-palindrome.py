class Solution:
    def isPalindrome(self, s: str) -> bool:
        compare=""
        for i in s:
            if i.isalnum():
                compare +=i.lower()
        return compare==compare[::-1]
        