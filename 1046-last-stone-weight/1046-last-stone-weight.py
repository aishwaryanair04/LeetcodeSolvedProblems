class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-num for num in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            if b > a:
                heapq.heappush(stones, -(b - a))
            elif a > b:
                heapq.heappush(stones, -(a - b))
        
        if len(stones) == 0:
            return 0
        else:
            return -(stones[0])
        
        
        