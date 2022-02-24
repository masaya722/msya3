N, M = map(int, input().split())
edges = []
for _ in range(N):
    edges.append([])
for _ in range(M):
    u, v = map(int, input().split())
    edges[u - 1].append(v - 1)
    edges[v - 1].append(u - 1)

def dfs(i, prev):
    global seen
    global flag
    seen[i] = True
    for nexti in edges[i]:
        if nexti != prev:
            if seen[nexti]:
                flag = False
            else:
                dfs(nexti, i)


seen = [False for _ in range(N)]

count = 0
for i in range(N):
    if not seen[i]:
        flag = True
        dfs(i, -1)
        if flag:
            count += 1

print(count)
