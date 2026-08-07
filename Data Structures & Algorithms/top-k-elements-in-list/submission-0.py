from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=Counter(nums).items()
        l=[y[0] for y in sorted(l,key= lambda x :x[1],reverse=True)]
        return [l[x] for x in range(k)]