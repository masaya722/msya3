D = int(input())
N = input()
mod = 1000000007

lenN = len(N)
dp = [[[0 for _ in range(2)] for _ in range(D)] for _ in range(lenN + 1)]

dp[0][0][0] = 1

for i in range(lenN):
    for j in range(D):
        for k in range(10):
            dp[i + 1][(j + k) % D][1] += dp[i][j][1]
            dp[i + 1][(j + k) % D][1] %= mod
        for k in range(int(N[i])):
            dp[i + 1][(j + k) % D][1] += dp[i][j][0]
            dp[i + 1][(j + k) % D][1] %= mod
        dp[i + 1][(j + int(N[i])) % D][0] += dp[i][j][0]
        dp[i + 1][(j + int(N[i])) % D][0] %= mod
print((dp[lenN][0][1] + dp[lenN][0][0] - 1))
