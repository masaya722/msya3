from collections import deque
N = int(input())
A= []
for i in range(N):
    a = int(input())
    A.append((a,i))
A.sort()
B = []
for i in range(N-1):
    a1,n1 = A[i]
    a2,n2 = A[i+1]
    if i ==0:
        B.append((n1,0))
        if a1==a2:
            B.append((n2,0))
        else:
            B.append((n2,1))
    else:
        n3,a3 = B.pop()
        if a1 ==a2:
            B.append((n3,a3))
            B.append((n2,a3))
        else:
            B.append((n3,a3))
            B.append((n2,a3+1))
B.sort()
for n,a in B:
    print(a)          




