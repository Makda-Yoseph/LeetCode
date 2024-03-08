class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        indx = bisect_left(arr,x)
        # print(arr[indx])
        print(indx)
        ans = []
        if indx<=len(arr)-1:
            l = indx-1
            r = indx
            # print(r)
            while k>0:
                print(0)
                if l>=0 and r<=len(arr)-1:
                    print(1)
                    if abs(arr[l]-x) <= abs(arr[r]-x):
                        print(12)
                        ans.append(arr[l])
                        l-=1
                    elif  abs(arr[l]-x) > abs(arr[r]-x):
                        print(13)
                        ans.append(arr[r])
                        r+=1
                elif r>(len(arr)-1):
                    print(2)
                    ans.append(arr[l])
                    l-=1
                elif l<0:
                    print(3)
                    ans.append(arr[r])
                    r+=1
                k-=1
        else:
            if x>arr[-1]:
                ans = arr[len(arr)-k:]
            else:
                ans = arr[:k]
        ans.sort()

        return ans


                




               

                


