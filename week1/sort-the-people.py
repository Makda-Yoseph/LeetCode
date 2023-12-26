class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            hm = i
            for j in range(i+1,len(heights)):
                if heights[j] > heights[i]:
                    tmp = heights[j]
                    heights[j] = heights[i]
                    heights[i] = tmp
                    tmpn = names[i]
                    names[i]= names[j]
                    names[j] = tmpn
                    if i ==j:
                        continue
                    
        
        return names
        
        


        