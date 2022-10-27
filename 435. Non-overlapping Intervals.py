class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        prev_end = -math.inf
        ans = 0
        for start,end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                ans +=1
        return ans
                
