"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key= lambda x : x.start)
        stack=[intervals[0]]
        for x in intervals[1:]:
            start=max(stack[-1].start,x.start)
            end=min(stack[-1].end,x.end)
            if start<end:
                return False
            stack.append(x)
        return True