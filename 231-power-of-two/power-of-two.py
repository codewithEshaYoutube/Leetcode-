class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def power(x):
            # base case
            if x==1:
                return True
            # recursiv ecas
            if x<=0 or x%2!=0:
                return False
            return (power(x//2))
        return power(n)
        #T:O(log n)
        #S;O(log n)
            