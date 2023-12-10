class Solution(object):
    def addSpaces(self, s, spaces):
        result = []
        sp = set(spaces)
        for i,c in enumerate(s):
            if i in sp:
                result.append(" ")
            result.append(c)
        return "".join(result)