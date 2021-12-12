import math
N = int(input())
A = list(map(int,input().split()))
A.sort()

if A.count(A[0]) ==N:
    print(A[0])
    exit()
flag1 = True
tmp = 0
for i in range(1,N):
    tmp = math.gcd(A[i],A[0])
    if math.gcd(A[i],A[0]) ==1:
        flag1 = False
flag2 = False
for a in A:
    if a%2 ==1:
        flag2 = True
flag3 = False
for i in range(1,N):
    if A[i]%A[0] !=0:
        flag3 = True
if flag1:
    print(tmp)
elif not flag1 and flag2 and flag3:
    print(1)
elif not flag1 and not flag2 and flag3:
    print(A[0])
elif not flag1 and flag2 and not flag3:
    print(2)
else:
    print(A[0])
