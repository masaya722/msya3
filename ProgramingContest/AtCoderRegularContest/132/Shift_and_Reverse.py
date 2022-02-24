from collections import deque
N = int(input())
P = list(map(int, input().split()))
INF = 10**18

rev = 1 if P[0]>P[1] or (N>2 and P[1]>P[2]) else 0
idx = P.index(1)
dist = [[INF for _ in range(N)]for _ in range(2)]
dist[rev][idx] = 0

que = deque()
que.append((rev,idx))

def update(rev,idx,val):
    global dist
    if dist[rev][idx]<=val:
        return
    else:
        dist[rev][idx] = val+1
        que.append((rev,idx))

while que:
    rev,idx = que.popleft()
    update(rev,(idx+N-1)%N,dist[rev][idx])
    update(1 if rev ==0 else 0,N-idx-1,dist[rev][idx])
print(dist[0][0])