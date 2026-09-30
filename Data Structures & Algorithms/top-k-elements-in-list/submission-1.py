class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)
        heap = []
        res = []

        for key, val in counts.items():
            heapq.heappush(heap, (-val, key))
        
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res
