N = int(input())
A = list(map(int, input().split()))

INF = 10**9+7

# dp[i][j] :インデックスでi番目まで計算し、i番目の符号がjのときの合計値
dp = [[0]*2 for _ in range(N)]
dp[0][0] =dp[0][1] =A[0]
plus = 1
minus = 1
if N ==1:
    print(A[0]) 
else:
    dp[1][0] = A[0] + A[1]
    dp[1][1] = A[0] -A[1]
    for i in range(1,N-1):
        dp[i+1][0] = dp[i][0] + plus*A[i+1] + dp[i][1] +minus*A[i+1]
        dp[i+1][1] = dp[i][0]-plus*A[i+1]
        tmp = plus
        plus+=minus
        minus =tmp
    
    print(sum(dp[N-1])%INF)
