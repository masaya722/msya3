N,W = map(int,input().split())
ws = []
vs = []
INF = -10**18
for i in range(N):
    w,v = map(int,input().split())
    ws.append(w)
    vs.append(v)
values =[[INF]*(W+1) for _ in range(N+1)]
values[0][0] = 0
for i in range(1,N+1):
    for j in range(W+1):
        values[i][j] = max(values[i][j], values[i-1][j])
        if j >=ws[i-1]:
            values[i][j] = max(values[i][j], values[i-1][j-ws[i-1]] + vs[i-1])
print(max(values[N]))
