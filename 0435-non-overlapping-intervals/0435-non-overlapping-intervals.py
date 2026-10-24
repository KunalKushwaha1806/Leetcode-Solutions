class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return []
        intervals.sort(key = lambda x:x[1])
        remove=0
        curr_end=intervals[0][1]

        for start , end in intervals[1:]:
            if start>=curr_end:
                curr_end=end
            else:
                remove+=1

        return remove