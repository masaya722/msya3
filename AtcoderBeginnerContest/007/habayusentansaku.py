from collections import deque

R, C = list(map(int, input().split()))
sy, sx = list(map(int, input().split()))
gy, gx = list(map(int, input().split()))
S = []
for i in range(R):
    s = input()
    S.append(s)

# 1始まりの入力を0始まりに直す
sy -= 1
sx -= 1
gy -= 1
gx -= 1

# 始点からの最終稼働回数を管理する2次元配列。-1であれば未訪問であることを表す
dist = []
for i in range(R):
    dist.append([-1] * C)

# キューを用意して、始点を入れる
Q = deque()
Q.append([sy, sx])
dist[sy][sx] = 0

# キューを取り出しながら探索する
while len(Q) > 0:
    i, j = Q.popleft()
    # 4つの隣マスを確認する
    for i2, j2 in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
        if not (0 <= i2 < R and 0 <= i2 < C):
            continue
        # もし壁マスであれば無視する
        if S[i][j] == '#':
            continue
        # もし未訪問であれば、距離を更新してキューに入れる
        if dist[i2][j2] == -1:
            dist[i2][j2] = dist[i][j] + 1
            Q.append([i2, j2])

print(dist[gy][gx])
