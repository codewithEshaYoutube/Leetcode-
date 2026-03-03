class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        nums
        --> brute force
        each element + each other element
        compare target
        return index
        --> array 
        find out pair of element making target
        update in array
        --> hashmap
        target-num=complement
        9-2=7
        9-7=2
        9-11=-4
        9-15=6
        
        """
        hashmap={}
        n=len(nums)
        for i,num in enumerate (nums):
            
            complement=target-nums[i]
            
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[num]=i


        


       