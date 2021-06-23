N, M = map(int, input().split())
edge = []
for i in range(N):
    edge.append([])

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)


def dfs(i, prev):
    global flag
    global seen
    seen[i] = True
    for nexti in edge[i]:
        if nexti != prev:
            if seen[nexti]:
                flag = False
            else:
                dfs(nexti, i)


seen = [False for i in range(N)]
ans = 0
for i in range(N):
    if not seen[i]:
        flag = True
        dfs(i, -1)
        if flag:
            ans += 1

print(ans)