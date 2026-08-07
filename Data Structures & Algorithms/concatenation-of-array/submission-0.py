class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l=[]

        n=len(nums)

        for x in range (2*n):
            index=x%n
            l.append(nums[index])
        
        return l