class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        m=0
        j=len(heights)-1
        while(i<j):
            h=min(heights[i],heights[j])
            l=j-i
            cap=l*h
            m=max(m,cap)
            if heights[i]>=heights[j]:
                j-=1
            else:
                i+=1
        return m