class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common_set=set()
        for i in nums1:
            for j in nums2:
                if i==j:
                    common_set.add(i)
                
        return list(common_set)

        