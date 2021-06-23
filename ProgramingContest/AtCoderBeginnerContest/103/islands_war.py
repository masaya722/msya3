N, M = map(int, input().split())

islands = []
for _ in range(M):
    a, b = map(int, input().split())
    islands.append((b, a))
islands.sort()

x = 0
count = 0
for i in range(M):
    b, a = islands[i]
    if a > x:
        x = b - 1
        count += 1

print(count)