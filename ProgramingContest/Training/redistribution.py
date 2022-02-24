MOD = 10**9+7

S= int(input())
dp = [0]*(S+1)
dp[0] = 1
for i in range(1,S+1):
    for j in range(i-2):
        dp[i] += dp[j]
print(dp[S]%MOD)