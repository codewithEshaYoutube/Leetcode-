class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def back_track(nums_left,path):
            if not nums_left:
                res.append(path[:])
                return
            for i in range(len(nums_left)):
                n=nums_left.pop(0)
                path.append(n)
                back_track(nums_left,path)
                path.pop()
                nums_left.append(n)
        back_track(nums,[])
        unique=set(tuple(p)for p in res)
        return [list(p)for p in unique]

        