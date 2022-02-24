N = int(input())
A = list(map(int, input().split()))
INF = 10**9+7
dp = [[0]*2 for _ in range(N)]
dp[0][0] = dp[0][1] = A[0]
plus = 1
minus = 1
if N == 1:
    print(A[0])
else:
    dp[1][0] = A[0] + A[1]
    dp[1][1] = A[0] - A[1]
    for i in range(2, N):
        dp[i][0] = dp[i-1][0] + plus*A[i] + dp[i-1][1] + minus*A[i]
        dp[i][1] = dp[i-1][0] - plus*A[i]
        temp = plus
        plus += minus
        minus = temp
    print(sum(dp[N-1])%INF)
