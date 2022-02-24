N,W = map(int,input().split())
ws = []
vs = []
INF = 10**18
for i in range(N):
    w,v = map(int,input().split())
    ws.append(w)
    vs.append(v)
V = sum(vs)
weight = [[INF]*(V+1) for _ in range(N+1)]
weight[0][0] = 0
for i in range(1,N+1):
    for j in range(V+1):
        weight[i][j] = min(weight[i][j],weight[i-1][j])
        if j>=vs[i-1]:
            weight[i][j] = min(weight[i][j],weight[i-1][j-vs[i-1]]+ws[i-1])

ans = 0
for i in range(V+1):
    if W>=weight[N][i]:
        ans = i
print(ans)

