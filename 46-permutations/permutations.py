class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        """
        recursion/backtracking
        defining backtrack
        apply logic loop over len
        base case
        recursive call on each subproblem
        
        pop out the last
        append the elments at end
        save it in result 
        return
        """
        if (len(nums)==1):
            return [nums[:]]
        res=[]
        for i in range(len(nums)):
            num=nums.pop(0)
            perms=self.permute(nums)
            for perm in perms:
                perm.append(num)
            res.extend(perms)
            nums.append(num)
        return res
