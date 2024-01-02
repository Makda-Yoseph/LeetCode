class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        res = []
        while l<r:
            if numbers[r] + numbers[l] == target:
                res.append(l+1)
                res.append(r+1)
                
                break
            elif numbers[r] + numbers[l] > target:
                r -=1
            else:
                l+=1
        return res


        