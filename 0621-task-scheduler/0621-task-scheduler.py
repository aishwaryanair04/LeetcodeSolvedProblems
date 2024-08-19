class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        priority = []
        for task in set(tasks):
            freq = tasks.count(task)
            priority.append(-freq)
        heapq.heapify(priority)
        queue = deque()
        time = 0

        while priority or queue:
            time += 1
            if priority:
                a = heapq.heappop(priority) + 1
                if a != 0:
                    queue.append([(a), time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(priority, queue.popleft()[0])
        

        return time
        