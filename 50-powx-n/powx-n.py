class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            # Base case
            if n == 0:
                return 1
            # If n is negative, invert x and make n positive
            if n < 0:
                return 1 / power(x, -n)
            
            # Divide & conquer
            half = power(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        return power(x, n)
