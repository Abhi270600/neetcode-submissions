class TimeMap:

    def __init__(self):
        self.hashmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        
        n = len(self.hashmap[key])

        l, r = 0, n - 1

        best_val = ""
        
        while l <= r:

            mid = (l + r) // 2

            if self.hashmap[key][mid][1] == timestamp:
                return self.hashmap[key][mid][0]
            
            elif self.hashmap[key][mid][1] < timestamp:
                best_val = self.hashmap[key][mid][0]
                l = mid + 1
            
            else:
                r = mid - 1
        
        return best_val

