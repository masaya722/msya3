N, M = map(int, input().split())
edges = [[]for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)
used = [False]*N
ans = 1
col = [-1]*N


def dfs(v):
    global edges
    global vs
    if used[v]:
        return
    used[v] = True
    vs.append(v)
    for u in edges[v]:
        dfs(u)


def dfs2(i):
    global now
    global vs
    if i == len(vs):
        now += 1
        return
    v = vs[i]
    for c in range(3):
        col[v] = c
        ok = True
        for u in edges[v]:
            if col[u] == c:
                ok = False
        if not ok:
            continue
        dfs2(i+1)
    col[v] = -1


for i in range(N):
    vs = []
    if used[i]:
        continue
    dfs(i)
    col[vs[0]] = 0
    now = 0
    dfs2(1)
    ans *= now*3

print(ans)
