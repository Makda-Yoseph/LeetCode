class Solution:
    def reverseWords(self, s: str) -> str:
        words = list(s.split(" "))
        res = []
      
     
        for w in words[::-1]:
            if len(w) > 0:
                res.append(w)
       
        return " ".join(res)
        