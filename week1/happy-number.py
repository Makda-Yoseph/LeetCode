class Solution:
    def isHappy(self, n: int) -> bool:
        num = set()
        while n not in num:
            num.add(n)
            n = self.Sqno(n)
            if n == 1:
                return True
        return False
    def Sqno(self, n:int) -> int:
        p = 0
        while n != 0:
            d = (n % 10)**2
            p += d
            n = n// 10
        return p
         

            
        


            
        