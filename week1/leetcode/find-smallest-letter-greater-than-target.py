class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = bisect_right(letters,target)
        if n<len(letters):
            return letters[n]
        else:
            return letters[0]