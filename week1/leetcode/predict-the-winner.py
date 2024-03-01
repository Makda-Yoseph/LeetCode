class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        left = 0
        right = len(nums)-1
        turn = True
        def soln(left,right,turn):
            if left==right:
                if turn:
                    return[nums[left],0]
                else:
                    return [0,nums[left]]
            if turn:
                leftscore = soln(left+1,right,not turn)
                rightscore = soln(left,right-1,not turn)
                leftscore[0]+=nums[left]
                rightscore[0]+=nums[right]
                if leftscore[0]>rightscore[0]:
                    return leftscore
                else:
                    return rightscore
            else:
                leftscore = soln(left+1,right,not turn)
                rightscore = soln(left,right-1,not turn)
                leftscore[1]+=nums[left]
                rightscore[1]+=nums[right]
                if leftscore[1]>rightscore[1]:
                    return leftscore
                else:
                    return rightscore
        
        score = soln(left,right,turn)
        return score[0]>=score[1]

        