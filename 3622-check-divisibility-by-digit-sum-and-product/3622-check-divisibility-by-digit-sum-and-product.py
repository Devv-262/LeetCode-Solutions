class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x = []
        b = n
        while b!= 0 :
            r = b%10
            b = b // 10
            x.append(r)
        s  = math.prod(x) + sum(x)
        return n % s == 0
        