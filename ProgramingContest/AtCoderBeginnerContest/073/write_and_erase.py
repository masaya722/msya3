from collections import deque

N = int(input())

A =[]
for i in range(N):
    a = int(input())
    A.append(a)
A.sort()
Q = deque()
Q.append(A[0])

for i in range(N-1):
    if len(Q) != 0:
        a = Q.pop()
        if A[i+1] != a:
            Q.append(a)
            Q.append(A[i+1])
    else:
        Q.append(A[i+1])
    
print(len(Q))



