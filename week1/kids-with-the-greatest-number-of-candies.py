class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        great = max(candies)
        result = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= great:
                value = True
            else:
                value = False
            result.append(value)
        return result

        