n, m = map(int, input().split())
c = list(map(int, input().split()))
dp = list(range(n + 1))

for i in range(2, n + 1):
    for j in c:
        if j <= i and dp[i - j] + 1 < dp[i]:
            dp[i] = dp[i - j] + 1

print(dp[n])
