from bisect import bisect_right

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sumA = []
tmpA = 0
for i in range(N):
    tmpA += A[i]
    sumA.append(tmpA)
sumB = []
tmpB = 0
for i in range(M):
    tmpB += B[i]
    sumB.append(tmpB)

idx = bisect_right(sumB,K)
ans = idx
for i in range(N):
    if K>=sumA[i]:
        K-=sumA[i]
        ans =max(ans,bisect_right(sumB,K)+i+1)
        K+=sumA[i]
print(ans)