n, x = map(int, input().split())
ans = 0

while True:
    if n == 0 and x == 0:
        break
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                if x == i + j + k:
                    ans += 1
    n, x = map(int, input().split())
    print(ans)
    ans = 0
