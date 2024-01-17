class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre = [0]*len(s)
        print(97%26)
        for i in shifts:
            if i[2] ==1:
                pre[i[0]] += 1
            elif i[2] == 0:
                pre[i[0]] +=-1
            if i[1]+1 < len(s):
                if i[2] ==1:
                    pre[i[1]+1] += -1
                elif i[2] == 0:
                    pre[i[1]+1] +=1
            
        for i in range(1,len(pre)):
            pre[i] += pre[i-1]
        ans = []
        
        for j in range(len(s)):
            k = ((pre[j] + ord(s[j]) - 97) % 26) + 97  
            # k = k + 97 
            # if k> 122:
            #     k-=122
            #     k = k+96 
            ans.append(chr(k))  
        return (''.join(ans))

            