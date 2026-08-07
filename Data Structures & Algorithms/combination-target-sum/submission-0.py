class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(arr,sum,i):
            if sum==target:
                res.append(arr[:])
                return
            elif i>=len(nums) or sum>target:
                return
            arr.append(nums[i])
            backtrack(arr,sum+nums[i],i)
            arr.pop()
            backtrack(arr,sum,i+1)

        backtrack([],0,0)
        return res