class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap =[]
        
        for x,y in points:
            dist = math.sqrt(x*x + y*y)
            minHeap.append([dist,x,y])
        
        heapq.heapify(minHeap)
        res = []
        
        while len(res) < k:
            res.append(heapq.heappop(minHeap))
        
        final_res = []
        for x,y,z in res:
            final_res.append([y,z])
        return final_res
            
        
        
        
        
            
        