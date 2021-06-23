import sys

sys.setrecursionlimit(10 ** 6)
A = list()

for i in range(10):
    A.append(list(input()))


def search(i, j):
    if i < 0 or 9 < i or j < 0 or 9 < j or A[i][j] == 'x':
        return
    if reached[i][j] == 'o':
        return
    reached[i][j] = 'o'

    search(i - 1, j)
    search(i + 1, j)
    search(i, j - 1)
    search(i, j + 1)


flag = False

for i in range(10):
    for j in range(10):
        reached = [['x' for a in range(10)] for b in range(10)]
        if A[i][j] == 'x':
            A[i][j] = 'o'
            search(i, j)
            if reached == A:
                flag = True
                break
            A[i][j] = 'x'
    if flag:
        break

if flag:
    print('YES')
else:
    print('NO')
