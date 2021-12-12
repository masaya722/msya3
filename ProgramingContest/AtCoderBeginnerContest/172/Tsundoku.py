from bisect import bisect_right
N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
sumA = []
tmp1 =0
for i in range(N):
    tmp1+=A[i]
    sumA.append(tmp1)
sumB = []
tmp2 =0
for i in range(M):
    tmp2+=B[i]
    sumB.append(tmp2)
count = bisect_right(sumB,K)
ans = count
for i in range(N):
    if K>=sumA[i]:
        K-=sumA[i]
        while count >0 and K<sumB[count-1]:
            count-=1
        ans = max(ans,count+i+1)
        K+=sumA[i]
print(ans)