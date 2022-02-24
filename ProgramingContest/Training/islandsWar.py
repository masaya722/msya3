N, M = map(int, input().split())
islands = []
for _ in range(M):
    a, b = map(int, input().split())
    islands.append((b, a))

islands.sort()

x = 0
ans = 0
for i in range(M):
    b, a = islands[i]
    if x < a:
        x = b - 1
        ans += 1
print(ans)
