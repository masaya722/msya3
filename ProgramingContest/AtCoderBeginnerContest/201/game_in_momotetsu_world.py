h, w = map(int, input().split())
a = [list(map(lambda x: 1 if x == '+' else -1, list(input())))
     for _ in range(h)]
dp = [[-1]*w for _ in range(h)]
INF = 10**10
for y in reversed(range(0, h)):
    for x in reversed(range(0, w)):
        if (y, x) == (h-1, w-1):
            dp[y][x] = 0
        elif (x+y) % 2 == 0:
            ans = -INF
            if y < h-1:
                ans = max(ans, dp[y+1][x]+a[y+1][x])
            if x < w-1:
                ans = max(ans, dp[y][x+1]+a[y][x+1])
            dp[y][x] = ans
        else:
            ans = INF
            if y < h-1:
                ans = min(ans, dp[y+1][x] - a[y+1][x])
            if x < w-1:
                ans = min(ans, dp[y][x+1] - a[y][x+1])
            dp[y][x] = ans
if dp[0][0] >0:
    print("Takahashi")
elif dp[0][0] <0:
    print("Aoki")
else:
    print("Draw")
