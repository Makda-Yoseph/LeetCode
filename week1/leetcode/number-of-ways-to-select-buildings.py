class Solution:
    def numberOfWays(self, s: str) -> int:
        zero = 0
        zero_one = [0]*len(s)
        for i in range(len(s)):
            if s[i] == '0':
                zero +=1
            else:
                zero_one[i] = zero
        one_zero = [0]*len(s)
        one = 0
        for i in range(len(s)):
            if s[i] == '1':
                one +=1
            else:
                one_zero[i] = one
        r_zero=r_one=0
        suffix_zero_one =[]
        e = len(s)-1
        for j in range(len(s)) :
            if s[e] == '0':
                r_zero +=1
            suffix_zero_one .append(r_zero)
            e -=1
        suffix_zero_one.reverse()
        suffix_one_zero = []
        d = len(s)-1
        for j in range(len(s)) :
            if s[d] == '1':
                r_one +=1
            suffix_one_zero.append(r_one)
            d -=1
        suffix_one_zero.reverse()
        count = 0
        for k in range(len(suffix_one_zero)):
            count+= suffix_one_zero[k]*one_zero[k] + suffix_zero_one[k]*zero_one[k]
        return count
        