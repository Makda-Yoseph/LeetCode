class Solution:
    def sortSentence(self, s: str) -> str:
        dic ={}
        res = []
        strings = list(map(str,s.split()))
        for i in strings:
            k = 1
            dic[int(i[-1])] = i[:len(i)-1]
            k +=1
        for n in range(1,len(strings)+1):
            res.append(dic[n])
        return " ".join(res)
            

        
        