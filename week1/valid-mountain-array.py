class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        id = 0
        flag = 1
        if len(arr)<3:
            return False
        if arr[1]<=arr[0]:
            return False
        for i in range(len(arr)-1):
            if arr[i+1]> arr[i]:
                continue
            else:
                flag = 0
                id = i
                break
        if flag == 0:
            f = 0
            for i in range(id,len(arr)-1):
                if arr[i+1]<arr[i]:
                    continue
                else:
                    f = 1
                    break
            if f ==1:
                return False
            else:
                return True
        else:
            return False

        