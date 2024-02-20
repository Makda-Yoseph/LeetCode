class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        for a,b in costs:
            diff.append([b-a,a,b])
        diff.sort(reverse = True)
        total = 0
        for i in range(len(costs)):
            if i< len(costs)/2:
                total += diff[i][1]
            else:
                total += diff[i][2]
        # print(diff)
        return total
         