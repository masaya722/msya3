W = int(input())
N, K = map(int, input().split())
dp = [[0 for _ in range(W+1)]for _ in range(K+1)]

for _ in range(N):
    a, b = map(int, input().split())
    for i in reversed(range(K)):
        for j in range(W+1):
            if j >= a:
                dp[i+1][j] = max(dp[i][j-a] + b, dp[i+1][j])

print(dp[K][W])
