from ast import While
from collections import deque
a,N = map(int,input().split())
Q = deque()
Q.append((1,0))
M =1
while M<N:
    M*=10
done = [False for _ in range(M)]
done[0] =True
cnt = 0
while Q:
    x,cnt = Q.popleft()
    if x ==N:
        print(cnt)
        exit()
    if x>M:
        continue
    if done[x]:
        continue
    done[x]=True
    Q.append((x*a,cnt+1))
    if x >10 and x%10!=0:
        stri = list(str(x))
        i = stri.pop()
        rev = int(i+''.join(stri))
        Q.append((rev,cnt+1))
print(-1)