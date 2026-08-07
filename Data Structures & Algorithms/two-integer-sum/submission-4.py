class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic=[]
        for x,y in enumerate(nums):
            dic.append([y,x])
        l=sorted(dic,key=lambda x: x[0])
        i=0
        j=len(nums)-1
        while(i<j):
            s=l[i][0]+l[j][0]
            if s == target:
                return sorted([l[i][1],l[j][1]])
            elif s>target:
                j-=1
            else:
                i+=1
        return []
            
