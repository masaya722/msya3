import bisect
N,Q = map(int,input().split())
A = list(map(int,input().split()))

C = []
for i in range(N):
    C.append(A[i]-(i+1))

for i in range(Q):
    K = int(input())
    idx = bisect.bisect_left(C,K)
    if idx ==N:
        print(A[N-1]+(K-C[N-1]))
    else:
        print(A[idx]-(C[idx]-K)-1)
