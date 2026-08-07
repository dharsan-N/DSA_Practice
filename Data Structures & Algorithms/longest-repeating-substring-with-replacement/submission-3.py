class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic={}
        i=0
        ans=float("-inf")
        for j,x in enumerate(s):
            dic[x]=dic.get(x,0)+1
            m=max(list(dic.values()))
            while(i<j and (j-i+1)-m>k):
                dic[s[i]]-=1
                i+=1
            ans=max(ans,j-i+1)
        return ans