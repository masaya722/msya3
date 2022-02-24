from collections import deque

n, x, y = list(map(int, input().split()))
x += 201
y += 201
obstacle = []
for _ in range(n):
    x1, y1 = map(int, input().split())
    x1 += 201
    y1 += 201
    obstacle.append((x1, y1))

dist = []
for _ in range(403):
    dist.append([-1] * 403)

Q = deque()
Q.append((201, 201))
dist[201][201] = 0

while len(Q) > 0:
    i, j = Q.popleft()
    for i1, j1 in [(i + 1, j + 1), (i, j + 1), (i - 1, j + 1), (i + 1, j), (i - 1, j), (i, j - 1)]:
        if not 0 <= i1 < 403 or not 0 <= j1 < 403:
            continue
        if not all(i != i2 or j != j2 for i2, j2 in obstacle):
            continue

        if dist[i1][j1] == -1:
            dist[i1][j1] = dist[i][j] + 1
            Q.append((i1, j1))
print(dist[x][y])
