class ATM:

    def __init__(self):
        self.val = [20,50,100,200,500]
        self.beg = [0]*5
    def deposit(self, banknotesCount: List[int]) -> None:
        self.beg = [a+b for a,b in zip(self.beg,banknotesCount)]

    def withdraw(self, amount: int) -> List[int]:
        self.out = [0]*5
        for i in range(4,-1,-1):
            self.out[i] = min(self.beg[i], amount// self.val[i])
            amount -= self.out[i]* self.val[i]
        if amount == 0:
            self.beg = [a-b for a,b in zip(self.beg,self.out)]
        return [-1] if amount else self.out           


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)