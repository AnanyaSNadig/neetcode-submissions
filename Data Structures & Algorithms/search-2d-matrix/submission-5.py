class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        top = 0
        bottom = ROWS - 1

        while top <= bottom:
            row = (top + bottom) // 2

            if target > matrix[row][-1]:
                top = row + 1

            elif target < matrix[row][0]:
                bottom = row - 1

            else:
                break

        if top > bottom:
            return False

        row = (top + bottom) // 2
        l, r = 0, COLS - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if target == matrix[row][m]:
                return True

            elif target < matrix[row][m]:
                r = m - 1

            else:
                l = m + 1

        return False
