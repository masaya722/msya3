N, K = map(int, input().split())
 
def tri(n):
    return n * (n + 1) // 2
 
for s in range(3 * (N - 1) + 1):
    if s <= N - 1:
        cnt = tri(s + 1)
    elif s <= 2 * (N - 1):
        cnt = N * N - tri(s - N + 1) - tri(2 * N - s - 2)
    else:
        cnt = tri(3 * N - 2 - s)
    if K <= cnt:
        for x in range(N):
            if s <= N - 1:
                c = max(0, s + 1 - x)
            elif s <= 2 * (N - 1):
                c = N - abs(x - (s - N + 1))
            else:
                c = max(0, 2 * N - 1 - s + x)
            if K <= c:
                for y in range(N):
                    if s - (N - 1) <= x + y <= s:
                        if K == 1:
                            print(x + 1, y + 1, s - x - y + 1)
                            exit(0)
                        K -= 1
            K -= c
    K -= cnt