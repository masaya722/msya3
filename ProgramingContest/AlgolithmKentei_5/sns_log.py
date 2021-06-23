N, Q = map(int, input().split())

# FalseのN×Nの2次元配列を作る
graph = []
for i in range(0, N):

    # 長さNのFalseの1次元配列を作る
    row = []
    for j in range(0, N):
        row.append(False)
    graph.append(row)

for i in range(0, Q):
    query = list(map(int, input().split()))
    a = query[1]-1
    if query[0] == 1:
        b = query[2]-1
        graph[a][b] = True

    if query[0] == 2:
        for v in range(0, N):
            if graph[v][a]:
                graph[a][v] = True

    if query[0] == 3:
        to_follow = []
        for v in range(0, N):
            if graph[a][v]:
                for w in range(0, N):
                    if graph[v][w] and w != a:
                        to_follow.append(w)
        for w in to_follow:
            graph[a][w]

for i in range(0, N):
    for j in range(0, N):
        # iからjへと辺がある場合はYを、辺がない場合はNを出力する。改行はしない
        if graph[i][j]:
            print('Y', end='')
        else:
            print('N', end='')
    print()
