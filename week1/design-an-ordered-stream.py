class OrderedStream:

    def __init__(self, n: int):
        self.num = n
        self.arr = [None] * n
        self.r , self.l = 0,0
    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey-1] = value
        while self.r < len(self.arr):
            if self.r == len(self.arr)-1 and self.arr[self.r]!= None:
                result = self.arr[self.l:]
                return result
            elif self.arr[self.r] != None:
                self.r +=1
            else:
                result = self.arr[self.l:self.r]
                self.l = self.r
                return result
            
        
        
 
                
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)