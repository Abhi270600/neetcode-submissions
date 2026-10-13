class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) >= 2:
            s1 = -heapq.heappop(heap)
            s2 = -heapq.heappop(heap)

            if s1 == s2:
                continue
            
            elif s1 < s2:
                heapq.heappush(heap, -(s2 - s1))
            
            else:
                heapq.heappush(heap, -(s1 - s2))
        
        return -heap[0] if heap else 0
