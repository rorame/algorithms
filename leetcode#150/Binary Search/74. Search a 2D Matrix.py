# my solution
def searchMatrix(matrix, target):
    row, col = len(matrix), len(matrix[0])

    top, bottom = 0, row-1

    while top <= bottom:
        mid = (bottom + top) // 2

        if matrix[mid][-1] == target:
            return True
        if matrix[mid][-1] > target:
            left, right = 0, len(matrix[mid]) - 1

            while left <= right:
                colMid = (right + left) // 2

                if matrix[mid][colMid] == target:
                    return True
                if matrix[mid][colMid] > target:
                    right = colMid - 1
                else:
                    left = colMid + 1

            bottom = mid - 1
        else:
            top = mid + 1
    return False

# neetcode's solution
def searchMatrix_neetcode(matrix, target):
    ROWS, COLS = len(matrix), len(matrix[0])

    top, bot = 0, ROWS - 1
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else: # значит таргет находится в нашей строке и нужно применять бинарный поиск для данной строки
            break

    if not (top <= bot): # мы перебрали все строки и нашего таргета не нашли
        return False
    row = (top + bot) // 2
    l, r = 0, COLS - 1
    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    return False


            

matrix = [[1,3,5]]

print(searchMatrix(matrix, target=1))
