from collections import deque

H, W = map(int, input().split())
board = [list(input()) for _ in range(H)]

blackFlags = [[-1] * W for _ in range(H)]

Q = deque()
for i in range(H):
    for j in range(W):
        if board[i][j] == '#':
            Q.append((i, j))
            blackFlags[i][j] = 0

cost = 0
while len(Q) > 0:
    i, j = Q.popleft()
    for i1, j1 in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if 0 <= i1 < H and 0 <= j1 < W:
            if blackFlags[i1][j1] == -1:
                Q.append((i1, j1))
                blackFlags[i1][j1] = blackFlags[i][j] + 1
                cost = blackFlags[i1][j1]

print(cost)
