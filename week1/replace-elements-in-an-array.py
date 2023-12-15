class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        count = dict((n, i) for i, n in enumerate(nums))
        
        for op in operations:
            if op[0] in count:
                nums[count[op[0]]] = op[1]
                count[op[1]] = count[op[0]]
                del count[op[0]]
        
        
        
        return nums