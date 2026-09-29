class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # O(nlogn) solution

        return sorted(s) == sorted(t)
