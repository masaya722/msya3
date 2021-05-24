from collections import deque

H, W = map(int, input().split())
board = [list(input()) for _ in range(H)]

# ボードの黒マスの数
black = 0
for i in range(H):
    for j in range(W):
        if board[i][j] == '#':
            black += 1

done = []
for i in range(H):
    done.append([False] * W)

cost = []
for i in range(H):
    cost.append([0] * W)

Q = deque()
Q.append([0,0])
flag = True
while flag:
    if len(Q) == 0:
        break
    i, j = Q.popleft()
    done[i][j] = True
    for i1, j1 in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if 0 <= i1 < H:
            if 0 <= j1 < W:
                if board[i1][j1] == '#':
                    continue
                if done[i1][j1]:
                    continue
                done[i1][j1] = True
                cost[i1][j1] = cost[i][j] + 1
                Q.append([i1, j1])
                if i1 == H - 1 and j1 == W - 1:
                    flag = False


if flag:
    print(-1)
else:
    print(H*W-cost[H - 1][W - 1]-black-1)
