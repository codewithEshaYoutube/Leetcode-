class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # common_set=set()
        # for i in nums1:
        #     for j in nums2:
        #         if i==j:
        #             common_set.add(i)   #T On*m
                
        # return list(common_set)
        """ solution 2"""
        # return list(set(nums1) & set(nums2))
        # T=O(n+m)
        # S=O(n+m)
        """ solution 3"""
        set1=set(nums1)
        set2=set(nums2)
        return list(set1 & set2)


        