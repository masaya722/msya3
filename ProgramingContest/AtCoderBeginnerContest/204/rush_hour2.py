N, M = map(int, input().split())

G = [[]*N]
for _ in range(M):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append((b, c, d))
    g[b].append((a, c, d))

def dist(c,dd,t):
    return c+dd//(t+1)

def dijkstra(start =0,INF = 10**18):
    from heapq import heappop,heappush
    d = [INF for _ in range(len(G))]
    d[start] = 0
    que = []
    heappush(que,(0,start))
    while que:
        d_,v = heappop(que)
        if d[v] <d_:
            continue
        for u,c,dd in G[v]:
            mincost = d[v] + dist(c,dd,d[v])
            dd2 = dd**0.5-1
            for i in range(4):
                d_ = dd2+i

