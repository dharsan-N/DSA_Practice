class Solution:
    def scoreOfString(self, s: str) -> int:
        score=0
        for x in range (len(s)-1):
            score+=abs(ord(s[x]) - ord(s[x+1]))
        
        print(score)
        return score