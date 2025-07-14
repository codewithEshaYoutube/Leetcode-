from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        USING counter
        loop
        check duplicates
        remove
        update set
        return
        """
        counter=Counter(nums)
        for num in counter:
            if counter[num]==1:
                return num

        




        