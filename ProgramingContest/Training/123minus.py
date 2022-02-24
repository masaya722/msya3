N = int(input())
ng1 = int(input())
ng2 = int(input())
ng3 = int(input())
ng = [ng1,ng2,ng3]
INF = 10**18
dp = [INF]*(N+1)
dp[N] =0
if N in ng:
    print("NO")
    exit()
for i in range(N,0,-1):
    for j in range(1,4):
        if i-j>=0:
            if i-j not in ng:
                dp[i-j] = min(dp[i-j],dp[i]+1)
if dp[0]>100:
    print("NO")
else:
    print("YES")
        