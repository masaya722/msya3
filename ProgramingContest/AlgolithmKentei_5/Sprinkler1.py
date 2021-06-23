N, M, Q = map(int, input().split())

# FalseのN×Nの2次元配列を作る
graph = []
for i in range(0, N):
    row = []
    for j in range(0, N):
        row.append(False)
    graph.append(row)

# M本の辺を受け取る
for i in range(0, M):
    u, v = map(int, input().split())

    u -= 1
    v -= 1

    graph[u][v] = True
    graph[v][u] = True

# 頂点の色のリストを受け取る
C = list(map(int, input().split()))

# Q個のクエリを受けとる
for i in range(0, Q):
    query = list(map(int, input().split()))

    # スプリンクラーを起動するクエリの場合
    if query[0] == 1:
        x = query[1]
        x -= 1
        print(C[x])
        # 全ての頂点を順番に見る
        for i in range(0, N):
            if graph[x][i]:
               C[i] = C[x]

    # スプリンクラーを起動しないクエリの場合
    if query[0] == 2:
        x = query[1]
        y = query[2]
        x -= 1
        print(C[x])
        C[x] = y