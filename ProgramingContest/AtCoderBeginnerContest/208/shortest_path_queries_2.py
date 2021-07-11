import sys
sys.setrecursionlimit(10**8)

N,M= map(int,input().split())
INF = 10**18
dist = [[INF]*N for _ in range(N)]
for i in range(M):
    a,b,c = map(int,input().split())
    a -=1
    b -=1
    dist[a][b] = c

for i in range(N):
    dist[i][i] = 0

ans = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
            if dist[i][j] != INF:
                ans +=dist[i][j]
print(ans)
