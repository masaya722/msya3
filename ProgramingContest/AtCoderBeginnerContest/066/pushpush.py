from collections import deque
n = int(input())
a = list(map(int,input().split()))
Q = deque()
for i in range(n):
    if i%2==0:
        Q.appendleft(a[i])
    else:
        Q.append(a[i])
if n%2==1:
    print(*Q)
else:
    Q.reverse()
    print(*Q)