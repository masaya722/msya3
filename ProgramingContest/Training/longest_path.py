import sys
sys.setrecursionlimit(10**8)

N,M = map(int,input().split())

roads = [[]for _ in range(N)]
indeg = [0 for _ in range(N)]
for i in range(M):
    x,y = map(int,input().split())
    x -=1
    y -=1
    roads[x].append(y)
    indeg[y]+=1

dist = [0 for _ in range(N)]
done = [False]*N
def calc_dist(i):
    if done[i]:
        return dist[i]
    dist[i] = 0
    for j in roads[i]:
        dist[i] = max(dist[i],calc_dist(j)+1)
    done[i] = True
    return dist[i]
for i in range(N):
    if indeg[i] == 0:
        calc_dist(i)

print(max(dist))

