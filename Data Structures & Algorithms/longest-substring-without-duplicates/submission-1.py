class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r = 0, 0
        window = set()
        longest = 0

        while r < len(s):

            while s[r] in window:
                window.remove(s[l])
                l += 1

            window.add(s[r])
            r += 1

            longest = max(longest, len(window))

        return longest
