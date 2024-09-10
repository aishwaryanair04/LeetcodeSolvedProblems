class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        minHeap = []
        for n in freq:
            minHeap.append([freq[n], -n])
        
        heapq.heapify(minHeap)
        print(minHeap)
        
        res = []
        while minHeap:
            val = heapq.heappop(minHeap)
            res += [-val[1]]*val[0]
        
        return res
            
            
        
            
            
        
        
            
            
            
        
#         freq = Counter(nums)
#         nums.sort(key = lambda x: (freq[x], -x))
#         return nums
            
            
            
            
        
        
        
        
        