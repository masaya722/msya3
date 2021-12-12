h,n =map(int,input().split())
INF = 10**18
dp = [INF for _ in range(2*(10**4)+1)]
dp[0] = 0
for i in range(n):
    a,b =map(int,input().split())
    for j in range(h):
        nh = a+j
        dp[nh] = min(dp[nh],dp[j]+b)
ans = dp[h]
for i in range(h,2*(10**4)):
    ans = min(ans,dp[i+1])
print(ans)