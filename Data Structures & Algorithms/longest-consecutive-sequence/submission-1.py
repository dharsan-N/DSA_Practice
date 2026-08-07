class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        l = set(nums)
        m = 0
        
        for x in l:
            # FIX 1: Check 'l' (the set), not 'nums' (the list)
            if x - 1 not in l:
                current_num = x
                current_streak = 1 
                
                while (current_num + 1 in l):
                    current_num += 1
                    current_streak += 1
                
                m = max(m, current_streak)
                
        return m