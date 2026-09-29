class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # O(n) solution

        if len(s) != len(t):
            return False

        hashmap = collections.defaultdict(int)

        for c in s:
            hashmap[c] += 1
        
        for c in t:
            hashmap[c] -= 1

        for k, v in hashmap.items():
            if v != 0:
                return False
        
        return True
