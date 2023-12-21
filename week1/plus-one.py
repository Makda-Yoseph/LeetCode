class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nine = 0
        for i in reversed(range(len(digits))):
            
            if digits[i] == 9:
                nine +=1
                digits[i] = 0
            else :
                digits[i] +=1
                break
           
        if nine == len(digits):
            digits.insert(0,1)

       
                
        return digits
            


        