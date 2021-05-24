N = int(input())
tree = [[]for _ in range(N)]
for _ in range(N-1):
    u,v,w = map(int,input().split())
    tree[u-1].append((v-1,w))
    tree[v-1].append((u-1,w))

from collections import deque
q = deque([(0,0)])
dists = [0]*N
done = [0]*N
while q:
    v,dist = q.popleft()
    done[v] = 1
    dists[v] = dist
    for nv,ndist in tree[v]:
        if not done[nv]:
            newdist = ndist^dist
            q.append((nv,newdist))

ans = 0
mod = 10**9+7
for i in range(60):
    bit = 1<<i
    zero = 0
    one = 0
    for j in range(N):
        if dists[j]&bit:
            one +=1
        else:
            zero+=1
    ans+=bit*zero*one%mod
ans %= mod
print(ans)