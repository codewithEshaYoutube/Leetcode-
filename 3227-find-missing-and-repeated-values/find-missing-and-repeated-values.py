from collections import Counter
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nums=[num for row in grid for num in row]
        n=len(grid)
        freq=Counter(nums)
        missing=repeated=-1
        for x in range(1,n*n+1):
            if freq[x]==2:
                repeated=x
            elif freq[x]==0:
                missing=x
        return[repeated,missing]
        #T: O(n2)
        #S: O(n2)

        