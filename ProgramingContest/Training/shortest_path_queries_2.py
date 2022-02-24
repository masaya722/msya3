N,M = map(int,input().split())
INF = 10**18
cost =[[INF]*N for _ in range(N)]
for i in range(M):
    a,b,c = map(int,input().split())
    cost[a-1][b-1] = c

for i in range(N):
    cost[i][i] = 0

ans = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            cost[i][j] = min(cost[i][j],cost[i][k]+cost[k][j])
            if cost[i][j] != INF:
                ans +=cost[i][j]
print(ans)
