class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        def sum_squares(n):

            res = 0

            while n:
                res += (n % 10) * (n % 10)
                n = n // 10
            
            return res


        while n > 1:
            
            n = sum_squares(n)
            
            if n in seen:
                return False
            
            seen.add(n)
        
        return True