class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        S:O(1)
        T:O(n)
        1,dictionary
        2, make a loop 
        3.check the duplicate
        4.we can emoinate the duplicates
        5. return array
        """
        nums_set=set()
        for n in nums:
            if n in nums_set:
                nums_set.remove(n)
            else:
                nums_set.add(n)
        return nums_set.pop()

        
                

        