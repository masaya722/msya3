from collections import deque
N,W = map(int,input().split())
S = []
INF = 10**18
for i in range(N):
    a,b = map(int,input().split())
    S.append((a,b))
S.sort(reverse=True)
Q = deque(S)
ans = 0
while W>0 and Q:
    a,b = Q.popleft()
    if W>=b:
        W-=b
        ans+=a*b
    else:
        ans+=a*W
        W=0
print(ans)
