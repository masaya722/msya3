N = int(input())
A = list(map(int,input().split()))
A.sort()

ttl = N
eater = A[0]
last = 0
for i in range(1,N):
    if A[i]<=eater*2:
        eater+=A[i]
    else:
        ttl-=i-last
        last = i
        eater+=A[i]
print(ttl)

