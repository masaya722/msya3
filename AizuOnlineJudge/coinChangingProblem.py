# test
n, m = map(int, input().split())
C = list(map(int, input().split()))
C.sort()

dp = list(range(n + 1))

for i in range(1, n + 1):
    for j in C:
        if j <= i and dp[i - j] + 1 < dp[i]:
            dp[i] = dp[i - j] + 1

print(dp[n])
