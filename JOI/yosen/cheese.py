from collections import deque

H, W, N = map(int, input().split())
town = [list(input()) for _ in range(H)]
factories = [[-1, -1] for i in range(N + 1)]

for i in range(H):
    for j in range(W):
        if town[i][j] == 'S':
            factories[0] = [i, j]
            continue
        for k in range(1, N + 1):
            if town[i][j] == str(k):
                factories[k] = [i, j]


def distances(s, g):
    done = [[False for _ in range(W)] for _ in range(H)]
    cost = [[0 for _ in range(W)] for _ in range(H)]
    Q = deque()
    Q.append(s)
    done[s[0]][s[1]] = True
    i2, j2 = g
    while len(Q) > 0:
        i, j = Q.popleft()
        for i1, j1 in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= i1 < H:
                if 0 <= j1 < W:
                    if town[i1][j1] == "X":
                        continue
                    if done[i1][j1]:
                        continue
                    done[i1][j1] = True
                    cost[i1][j1] = cost[i][j] + 1
                    Q.append([i1, j1])

                    if i1 == i2 and j1 == j2:
                        return cost[i1][j1]


ans = 0
for i in range(N):
    ans += distances(factories[i], factories[i + 1])
print(ans)
