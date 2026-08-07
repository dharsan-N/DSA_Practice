class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for x in range (len(nums)):
            if x >0 and nums[x-1]==nums[x]:
                continue
            left=x+1
            right=len(nums)-1
            while(left<right):
                if nums[x]+nums[left]+nums[right]==0:
                    res.append([nums[x],nums[left],nums[right]])
                    right-=1
                    left+=1
                    while(left<right and nums[left-1]==nums[left]):
                        left+=1
                    while(left<right and nums[right]==nums[right+1]):
                        right-=1
                elif  nums[x]+nums[left]+nums[right]>0:
                    right-=1
                else:
                    left+=1
        return res