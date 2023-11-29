class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        mina = len(prefix)
        s = ""
        flag = True
        for i in  range(len(strs)):
            mina = min(len(strs[i]),mina)
        for i in range(mina):
            for j in strs:
                if prefix[i] != j[i]:
                    flag = False
                    break
            if flag == True:
                s += prefix[i]
            else:
                break
        return s


                
            




        