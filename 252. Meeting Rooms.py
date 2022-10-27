class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x:x[1])
        prev_end = -math.inf
        for start,end in intervals:
            if start < prev_end:
                return False
            prev_end = end
        return True
