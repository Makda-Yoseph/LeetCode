class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        
        res = self.getRow(rowIndex-1)
        x = res [len(res) // 2 - 1]
        prefix = [res[0]]
        for i in range(1,ceil(len(res)/2)):
                # p += res[i]
                prefix.append(res[i-1] +res[i])
        if rowIndex%2==0:
            
            
            prefix.append(2*x)
            for i in range(len(prefix)-2,-1,-1):
                prefix.append(prefix[i])
           
        else:
            for i in range(len(prefix)-1,-1,-1):
                prefix.append(prefix[i])
        return prefix
