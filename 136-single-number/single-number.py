class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        for n in freq:
            if freq[n]==1:
                return n
            