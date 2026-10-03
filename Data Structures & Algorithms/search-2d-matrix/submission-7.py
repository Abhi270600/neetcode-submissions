class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS - 1

        while l <= r:

            row = (l + r) // 2

            if target < matrix[row][0]:
                r = row - 1
            
            elif target > matrix[row][-1]:
                l = row + 1
            
            else:
                break
        
        l, r = 0, COLS - 1

        while l <= r:

            mid = (l + r) // 2

            if target == matrix[row][mid]:
                return True
            
            elif target < matrix[row][mid]:
                r = mid - 1
            
            else:
                l = mid + 1
        
        return False
            
