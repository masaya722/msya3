import sys

sys.setrecursionlimit(1000000)
H, W = map(int, input().split())
town = []
for _ in range(H):
    c = input()
    town.append(c)

visited = []
for _ in range(H):
    visited.append([False] * W)

for row in range(H):
    for col in range(W):
        if town[row][col] == 's':
            sRow, sCol = row, col
        elif town[row][col] == 'g':
            gRow, gCol = row, col


def dfs(i, j):
    for i1, j1 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if not 0 <= i1 < H or not 0 <= j1 < W:
            continue
        if town[i][j] == '#':
            continue
        visited[i][j] = True
        if not visited[i1][j1]:
            dfs(i1, j1)


dfs(sRow, sCol)
if visited[gRow][gCol]:
    print('Yes')
else:
    print('No')
