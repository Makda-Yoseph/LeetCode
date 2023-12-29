class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        s = []
        d = dict((n,i) for i,n in enumerate(arr2))
        sa2 = set(arr2)
        for i in arr1:
            if i in sa2:
                s.append([d[i],i])
            else:
                s.append([float('inf'),i])
        j = sorted(s)
        k = []
        for i,m in j:
            k.append(m)

        return k
        