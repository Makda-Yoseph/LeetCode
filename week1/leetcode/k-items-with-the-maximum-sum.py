class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        count = 0
        if k <= numOnes:
            count += k
        elif k > numOnes:
            count +=numOnes
            k-= numOnes
            if k <= numZeros:
                count +=0
                
            else:
                k -= numZeros
                count -= k
        return count