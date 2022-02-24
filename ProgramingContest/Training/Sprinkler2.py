N, M, Q = map(int, input().split())
graph = []
for _ in range(0, N):
    row = []
    graph.append(row)

for _ in range(0, M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

C = list(map(int, input().split()))

for i in range(0, Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        x -= 1
        print(C[x])
        for j in graph[x]:
            C[j] = C[x]
    if query[0] == 2:
        x = query[1]
        x -= 1
        y = query[2]
        print(C[x])
        C[x] = y
