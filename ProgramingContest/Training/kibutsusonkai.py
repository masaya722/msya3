from collections import deque

H, W = map(int, input().split())

town = [list(input()) for _ in range(H)]

coll = [[3] * W for _ in range(H)]
Q = deque()
for i in range(H):
    for j in range(W):
        if town[i][j] == 's':
            Q.append((i, j))
            coll[i][j] = 0

while len(Q) > 0:
    i, j = Q.popleft()
    for i1, j1 in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if 0 <= i1 < H and 0 <= j1 < W:
            if coll[i1][j1] == 3:
                if town[i1][j1] == 'g':
                    print("YES")
                    exit()
                if town[i1][j1] == '#':
                    if coll[i][j] < 2:
                        coll[i1][j1] = coll[i][j] + 1
                        Q.append((i1, j1))
                else:
                    coll[i1][j1] = coll[i][j]
                    Q.appendleft((i1, j1))

print("NO")
