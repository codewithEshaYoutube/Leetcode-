class Solution:
    def twoSum(self, nums, target):
        Esha = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in Esha:
                return [Esha[complement],i]

            Esha[num] = i 
        return []
       
 


       
