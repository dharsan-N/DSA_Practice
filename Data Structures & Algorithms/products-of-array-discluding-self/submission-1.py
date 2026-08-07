class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1]*len(nums)
        prefix=1
        suffix=1
        n=len(nums)
        for x in range(n):
            result[x]=prefix
            prefix*=nums[x]
        suffix=1
        for x in range(n-1,-1,-1):
            result[x]*=suffix
            suffix*=nums[x]
        return result