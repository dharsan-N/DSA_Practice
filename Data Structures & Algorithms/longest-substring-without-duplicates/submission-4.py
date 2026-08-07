class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h=set()
        ans=0
        i=0
        for x in range(len(s)):
            while(s[x] in h):
                h.remove(s[i])
                i+=1
            h.add(s[x])

            ans=max(ans,x-i+1)
        
        return ans