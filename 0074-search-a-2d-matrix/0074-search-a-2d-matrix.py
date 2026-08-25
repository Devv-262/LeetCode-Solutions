class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target <= matrix[mid][m - 1]:
                low_r = 0
                high_r = m - 1
                while low_r <= high_r:
                    mid_r = (low_r + high_r) // 2

                    if matrix[mid][mid_r] == target:
                        return True
                    elif target < matrix[mid][mid_r]:
                        high_r = mid_r - 1
                    else:
                        low_r = mid_r + 1
                return False
            elif target > matrix[mid][m - 1]:
                low = mid + 1
            else:
                high = mid - 1
        return False