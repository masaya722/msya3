N, M, Q = list(map(int, input().split()))

graph = []
for _ in range(N):
    row = []
    for _ in range(N):
        row.append(False)
    graph.append(row)

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u][v] = True
    graph[v][u] = True

C = list(map(int, input().split()))

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x = query[1]-1
        print(C[x])
        for i in range(N):
            if graph[x][i]:
                C[i] = C[x]

    elif query[0] == 2:
        x = query[1]-1
        y = query[2]
        print(C[x])
        C[x] = y