class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        
    def addNum(self, num: int) -> None:
        if not self.maxheap and not self.minheap:
            heapq.heappush(self.maxheap, -num)
        
        else:
            if self.maxheap and num > -self.maxheap[0]:
                heapq.heappush(self.minheap, num)
            else:
                heapq.heappush(self.maxheap, -num)
        

        if abs(len(self.maxheap) - len(self.minheap)) > 1:
            if len(self.maxheap) > len(self.minheap):
                max_element = -heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, max_element)
            
            else:
                min_element = -heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, min_element)


    def findMedian(self) -> float:
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2
        
        else:
            if len(self.maxheap) > len(self.minheap):
                return -self.maxheap[0]
            else:
                return self.minheap[0]
        