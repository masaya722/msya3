import heapq

n,m = map(int,input().split())
G = [[] for _ in range(n)]
total = 0
for i in range(m):
    a,b,c = map(int,input().split())
    a-=1
    b-=1
    if c>0:
        total+=c
    G[a].append((c,b))
    G[b].append((c,a))
S= []
marked = [False for _ in range(n)]
marked[0] = True
marked_count = 1
for c,i in G[0]:
    heapq.heappush(S,(c,i))
while marked_count<n:
    c, i = heapq.heappop(S)
    if marked[i]:
        continue
    marked[i] = True
    marked_count+=1
    if c>0:
        total-=c
    for c,j in G[i]:
        heapq.heappush(S,(c,j))
print(total)