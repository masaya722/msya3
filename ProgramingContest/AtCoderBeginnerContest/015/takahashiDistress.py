W = int(input())
n, K = map(int, input().split())
dp = [[0 for _ in range(W + 1)] for _ in range(K + 1)]
for i in range(n):
    a, b = map(int, input().split())
    for j in reversed(range(1, K + 1)):
        for k in range(W + 1):
            if k >= a:
                dp[j][k] = max(dp[j][k], dp[j - 1][k - a] + b)
print(dp[K][W])