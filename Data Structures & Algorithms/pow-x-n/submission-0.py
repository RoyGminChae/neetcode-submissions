class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        val = 1
        if n > 0:
            for _ in range(n):
                val *= x

        if n < 0:
            for _ in range(n * -1):
                val /= x

        return val