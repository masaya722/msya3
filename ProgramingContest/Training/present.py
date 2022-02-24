from bisect import bisect_left

N = int(input())
box = sorted([[int(x) for x in input().split()] for _ in range(N)], key=lambda x: (x[0], -x[1]))

INF = 1e6
dp = [INF] * N

for w in [x[1] for x in box]:
    idx = bisect_left(dp, w)
    dp[idx] = w

print(bisect_left(dp, INF))
