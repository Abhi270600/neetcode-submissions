class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        hashmap = {")": "(", "]": "[", "}": "{"}

        for ch in s:

            if stack and ch in hashmap:
                if stack[-1] == hashmap[ch]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(ch)
        
        return True if not stack else False