import numpy as np


# Камни 2

n, m = map(int, input().split())

mat = np.zeros((n, m), dtype=str)

mat[0][0] = 'L'

for i in range(1, m):
    if i % 3 == 0:
        mat[0][i] = 'L'
    else:
        mat[0][i] = 'W'

for j in range(1, n):
    if j % 3 == 0:
        mat[j][0] = 'L'
    else:
        mat[j][0] = 'W'

for i in range(1, n):
    for j in range(1, m):
        if mat[i - 1][j - 1] == 'L':
            mat[i][j] = 'L'
        else:
            mat[i][j] = 'W'

print('Win' if mat[n-1][m-1] == 'W' else 'Loose')