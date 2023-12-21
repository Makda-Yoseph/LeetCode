class Bitset:

    def __init__(self, size: int):
        self.onth= set()
        self.zero = set(range(size))
        self.result = ['0']*size
    def fix(self, idx: int) -> None:
        self.onth.add(idx)
        if idx in self.zero:
            self.zero.remove(idx)
    def unfix(self, idx: int) -> None:
        self.zero.add(idx)
        if idx in self.onth:
            self.onth.remove(idx)
    def flip(self) -> None:
        temp = self.onth
        self.onth = self.zero
        self.zero = temp
        
    def all(self) -> bool:
         return len(self.zero) == 0

    def one(self) -> bool:
        return len(self.onth) != 0
        
    def count(self) -> int:
        return len(self.onth)

    def toString(self) -> str:
        for ones in self.onth:
            self.result[ones] = '1'
        for z in self.zero:
            self.result[z] = '0'
        return ''.join(self.result)
        




# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()