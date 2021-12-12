import heapq
n,m = map(int,input().split())
back_cnt = [0 for _ in range(n)]
pairs = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    a-=1
    b-=1
    pairs[a].append(b)
    back_cnt[b]+=1
ans = []
S= [i for i in range(n) if back_cnt[i]==0]
heapq.heapify(S)
while S:
    i = heapq.heappop(S)
    ans.append(i+1)
    for j in pairs[i]:
        back_cnt[j]-=1
        if back_cnt[j] ==0:
            heapq.heappush(S,j)
if len(ans) != n:
    print(-1)
else:
    print(*ans)