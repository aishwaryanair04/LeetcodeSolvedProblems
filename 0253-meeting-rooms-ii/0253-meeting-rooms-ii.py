class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start, end = [], []
        count = 0
        res = 0
        
        for s,e in intervals:
            start.append(s)
            end.append(e)
        
        start.sort()
        end.sort()
        
        i,j = 0,0
        
        while i < len(start):
            if start[i] < end[j]:
                i += 1
                count += 1
            elif end[j] <= start[i]:
                count -= 1
                j += 1
            res = max(res, count)
        return res
        
        
            
                
        