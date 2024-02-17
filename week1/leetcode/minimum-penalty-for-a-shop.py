class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix_n = [0]
        suffix_y = [0]
        pre = 0
        for p in range(len(customers)):
            if customers[p] =='N':
                pre +=1
            prefix_n.append(pre)

        e = len(customers)-1
        suf = 0
        for s in range(len(customers)):
            if customers[e] =='Y':
                suf +=1
            suffix_y.append(suf)
            e -=1
        suffix_y.reverse()
        res = []

        for i in range(len(prefix_n)):
            r =prefix_n[i]+suffix_y[i]
            res.append(r)
        look = float('inf')
        mini = 0
        for j in range(len(prefix_n)):
            if res[j]< look:
                mini = j
                look = res[j]
        return mini
