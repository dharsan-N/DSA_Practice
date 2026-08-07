from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        i=0
        dic={}
        target=Counter(t)
        res=s+t
        have=0
        need=len(target)
        for j,x in enumerate(s):
            if x in target.keys():
                dic[x]=dic.get(x,0)+1
                if dic[x]==target[x]:
                    have+=1
            while(i<=j and have==need):
                res=min(res,s[i:j+1],key=len)
                if s[i] in target.keys():
                    dic[s[i]]-=1
                    if dic[s[i]]<target[s[i]]:
                        have-=1
                i+=1
        if res==s+t:
            return ""
        return res
                