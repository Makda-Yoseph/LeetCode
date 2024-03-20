class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = [-1]*len(height)
        maxright = [-1]*len(height)
        stack1 = []
        stack2 = []
        for i in range(len(height)):
            if stack1 and stack1[-1]>=height[i]:
                maxleft[i]=stack1[-1]
            else:
                while stack1 and stack1[-1]<height[i]:
                    stack1.pop()
                stack1.append(height[i])
        print(maxleft)
        for j in range(len(height)-1,-1,-1):
            # print(j)
            if stack2 and stack2[-1]>=height[j]:
                maxright[j]=stack2[-1]
            else:
                while stack2 and stack2[-1]<height[j]:
                    stack2.pop()
                stack2.append(height[j])
            # print(stack2)
        ans=0
        l,r = 0,0
        for i in range(len(height)):
            if min(maxleft[l],maxright[r])-height[i]>0:
                ans+= min(maxleft[l],maxright[r])-height[i]
            l+=1
            r+=1
        return ans