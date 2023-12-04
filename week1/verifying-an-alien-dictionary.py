class Solution(object):
    def isAlienSorted(self, words, order):
        for i in range(len(words)-1):
            f,l= words[i],words[i +1]
            for j in range(len(f)):
                if j == len(l):
                    return False
                elif f[j] != l[j]:
                    if order.index(f[j]) > order.index(l[j]):
                        return False
                    break
        return True
        
        
        