class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom, row = 0, len(matrix) - 1, 0
        while top <= bottom:
            row = (top + bottom) // 2
            if target < matrix[row][0]: bottom = row - 1
            elif target > matrix[row][-1]: top = row + 1
            else: break
            
        top, bottom = 0, len(matrix[row]) - 1
        while top <= bottom:
            col = (top + bottom) // 2
            if target < matrix[row][col]: bottom = col - 1
            elif target > matrix[row][col]: top = col + 1
            else: return True

        return False