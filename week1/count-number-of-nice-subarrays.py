class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd = 0
        l,r = 0,0
        ct = 0
        while r< len(nums):
            if nums[r]%2!=0:
                odd +=1
            if odd >k:
                while odd > k:
                    if nums[l]%2!=0:
                        odd -=1
                    l+=1
            ct += r-l+1
            r+=1
       
        od2 = 0
        left,right= 0,0
        count = 0
        while right <len(nums):
            if (nums[right]%2)!=0:
                od2 +=1
            if od2>(k-1):
                while od2 >(k-1):
                    if (nums[left])%2 != 0:
                        od2-=1
                    left+=1
            count +=right - left +1
            right +=1
        return ct - count

            
        
        
