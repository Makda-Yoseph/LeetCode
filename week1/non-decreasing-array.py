class Solution(object):
    def checkPossibility(self, nums):
        flag = False
        if len(nums) == 1 or nums == sorted(nums):
            return True
        else:
            for i in range(len(nums)-1):
                if nums[i+1] >= nums[i]:
                    continue
                if flag == True:
                    return False
                if i == 0 or nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
                flag = True
            return flag
            

        