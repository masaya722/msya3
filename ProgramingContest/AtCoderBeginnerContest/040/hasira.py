N = int(input())
a = list(map(int, input().split()))
dp = [0 for _ in range(N)]
dp[0] = 0
dp[1] = abs(a[0]-a[1])
for i in range(2,N):
    dp [i] = min(abs(a[i]-a[i-2])+dp[i-2],abs(a[i]-a[i-1])+dp[i-1])
print(dp[N-1])