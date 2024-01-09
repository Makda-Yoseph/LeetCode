class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l,r = 0,0
        if len(typed) < len(name):
            return False
        while l < len(name) and r < len(typed):
            if name[l] == typed[r]:
                l+=1
                r+=1
            elif name[l] != typed[r]:
                if r ==0:
                    return False
                else:
                    if typed[r] == typed[r-1]:
                        r +=1
                    else:
                        return False
            if l >= len(name) and r < len(typed):
                while r< len(typed):
                    if name[-1] == typed[r]:
                        r+=1
                    else:
                        return False
            if l <=len(name)-1 and r >= len(typed):
                return False
        return True
                


        
        