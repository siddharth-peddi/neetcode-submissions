class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break
        
        if top > bottom:
            return False

        left = 0
        right = cols - 1

        while left <= right:
            middle = (left + right) // 2
        
            if matrix[mid][middle] == target:
                return True
            elif matrix[mid][middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return False