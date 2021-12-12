from collections import deque
MOD = 10**9+7
N,M = map(int,input().split())
cities = [[]for _ in range(N)]
for i in range(M):
    a,b = map(int,input().split()) 
    a-=1
    b-=1
    cities[a].append(b)
    cities[b].append(a)

dist = [-1]*N
dist[0] = 0
count = [0]*N
count[0] = 1
Q= deque()
Q.append(0)
while Q:
    i = Q.popleft()
    for j in cities[i]:
        if dist[j] ==-1:
            dist[j] =dist[i]+1
            Q.append(j)
            count[j] += count[i]
        elif dist[j] == dist[i]+1:
            count[j] += count[i]
print(count[N-1]%MOD)


