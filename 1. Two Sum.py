class Solution:
    def twoSum(self, nums, target):
        prev_map={} #hashmap value:index
        for i , n in enumerate(nums):
            diff=target-n
            
            if diff in prev_map:
                return[prev_map[diff],i] 
            prev_map[n]=i
        return


 


       
