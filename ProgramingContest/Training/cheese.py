from collections import deque

H, W, N = map(int, input().split())
town = [list(input()) for _ in range(H)]
factories = [[-1, -1] for _ in range(N + 1)]

for i in range(H):
    for j in range(W):
        if town[i][j] == "S":
            factories[0] = [i, j]
            continue
        for k in range(1, N + 1):
            if town[i][j] == str(k):
                factories[k] = [i, j]


def dfs(s, g):
    done = [[False] * W for _ in range(H)]
    cost = [[0] * W for _ in range(H)]
    g1, g2 = g
    Q = deque()
    Q.append(s)
    while len(Q)>0:
        i, j = Q.popleft()
        done[i][j] = True
        for i1, j1 in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= i1 < H and 0 <= j1 < W:
                if town[i1][j1] == "X":
                    continue
                if done[i1][j1]:
                    continue
                Q.append((i1, j1))
                cost[i1][j1] = cost[i][j] + 1
                if i1 == g1 and j1 == g2:
                    return cost[i1][j1]


ans = 0
for i in range(N):
    ans += dfs(factories[i], factories[i + 1])
print(ans)
