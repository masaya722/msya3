H, W = map(int, input().split())
A = []
for _ in range(H):
    A.append(input())

dp = [[0 for _ in range(W)]for _ in range(H)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if A[i][j] =='#':
            continue
        if i>0:
             dp[i][j] += dp[i-1][j]
        if j >0:
            dp[i][j] += dp[i][j-1]
print(dp[H-1][W-1]%(10**9+7))