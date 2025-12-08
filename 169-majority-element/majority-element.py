class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        

        Boyer Moree Algorithm
        # '''
        candidate=None
        count=0
        for i in nums:
            if count ==0:
                candidate=i
            if i==candidate:
                count+=1
            else:
                count-=1
        return candidate

        #s : O(1)
        #T: O(n)






        '''
        counter array
        loop over array
        check the element if found element increase the count
        return counter array
        '''
        
        # maj=max(nums)
        # n=len(nums)
        # count=[0]*(maj+1)

        # for i in nums:
        #     count[i]+=1
                
        #     if count[i]> n//2:
        #         return i    
        #S O(maj)  #T:O(n)
        