from collections import deque
n,m = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
Q = deque(A)
S = []
for i in range(m):
    b,c = map(int,input().split())
    S.append((c,b))
S.sort(reverse=True)
ans =0
cnt = 0
b = 0
while Q:
    i = Q.popleft()
    if b ==0:
        if cnt ==m:
            Q.append(i)
            break
        c,b = S[cnt]
        cnt+=1
    if c>i:
        ans+=c
        b-=1
    else:
        ans+=i
        b-=1
if Q:
    ans+=sum(Q)
print(ans)
        




