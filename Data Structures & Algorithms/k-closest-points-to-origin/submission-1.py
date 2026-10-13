class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        res = []

        for px, py in points:

            dist = math.sqrt((px * px) + (py * py))

            heapq.heappush(heap, (dist, px, py))
        
        while k:
            d, x, y = heapq.heappop(heap)
            res.append([x, y])
            k -= 1
        
        return res
