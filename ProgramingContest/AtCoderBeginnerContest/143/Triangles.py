from bisect import bisect_right
N = int(input())
L = list(map(int,input().split()))
L.sort()

dp = [[0 for _ in range(N)]for i in range(N)]
ans = 0
for i in range(N):
    for j in range(i+1,N):
        tmp = L[j]-L[i]
        idx = bisect_right(L,tmp)
        if idx<i:
            ans+=i-idx
print(ans)