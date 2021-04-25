N, M, Q = map(int, input().split())

# FalseのN×Nの2次元配列を作る
graph = []
for i in range(0, N):
    # 長さNのFalseの1次元配列を作る
    row = []
    graph.append(row)

# M本の辺を受け取る
for i in range(0, M):
    u, v = map(int, input().split())
    u = -1
    v = -1
    graph[u].append(v)
    graph[v].append(u)

# 頂点の色リストを受け取る
C = list(map(int, input().split()))

# Q個のクエリを受け取る
for i in range(0, Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        x -= 1

        print(C[x])
        for i in graph[x]:
            C[i] = C[x]

    if query[0] == 2:
        x = query[1]
        y = query[2]

        x -= 1
        print(C[x])
        C[x] = y
