class RandomizedSet:

    def __init__(self):
        self.res = []
        self.enum = {}
        self.count = 0
    def insert(self, val: int) -> bool:
        if val not in self.enum:
            self.res.append(val)
            self.enum[val] = self.count
            self.count +=1
            return True
        else:
            return False
        print(self.enum)

    def remove(self, val: int) -> bool:
        if val in self.enum.keys():
            i = self.enum[val]
            self.enum[self.res[-1]]= i
            tmp = self.res[-1]
            self.res[-1]=self.res[i]
            self.res[i] = tmp
            self.res.pop()
            self.count -=1
            del self.enum[val]
            return True
            
        else:
            return False
    def getRandom(self) -> int:
        return random.choice(self.res)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()