class Solution(object):
    def restoreString(self, s, indices):
        w = ""
        letters = {}
        for i in range(len(indices)):
            for l in range(len(s)):
                letters[indices[l]] = s[l]
        for i in range(len(indices)):
            w += letters[i]
        return w

