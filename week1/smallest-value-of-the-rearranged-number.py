class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        neg = 0
        if num < 0:
            num *= -1
            neg = 1

        n = []
        while num != 0:
            n.append(num % 10)
            num //= 10 
        n.sort()

        if len(n) == 1:
            if neg == 1:
                return n[0] * -1
            else:
                return n[0]
        elif n[0] == 0:
            l = 1
            while n[0] == 0 and l < len(n):
                if n[l] != 0:
                    n[l], n[0] = n[0], n[l]
                    break
                else:
                    l += 1

        if neg == 1:
            result = 0
            n.sort(reverse=True)
            for digit in n:
                result = (result * 10) + digit
            return result * -1

        result = 0
        for digit in n:
            result = (result * 10) + digit
        return result