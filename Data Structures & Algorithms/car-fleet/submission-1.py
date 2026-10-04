class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        temp = []
        stack = []

        for i in range(len(position)):
            temp.append([position[i], speed[i]])
        
        temp.sort(reverse = True)

        for p, s in temp:

            stack.append((target - p) / s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
