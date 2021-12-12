
from collections import deque,defaultdict
n,x,y = map(int,input().split())
G= [[]for _ in range(n)]
for i in range(n-1):
    G[i].append(i+1)
    G[i+1].append(i)
G[x-1].append(y-1)
G[y-1].append(x-1)
dict = defaultdict(int)
Q = deque()
done = [False for _ in range(n)]
dist = [[0 for _ in range(n)]for _ in range(n)]

for i in range(n):
    Q.append(i)
    while Q:
        j = Q.popleft()
        done[j] = True
        for k in G[j]:
            if done[k]:
                continue
            if dist[i][k] ==0:
                dist[i][k] = dist[i][j]+1
            else:
                dist[i][k] = min(dist[i][j]+1,dist[i][k])
            Q.append(k)
    for j in dist[i]:
        dict[j]+=1
    done = [False for _ in range(n)]
for i in range(n):
    if i==0:
        continue
    print(dict[i]//2)
