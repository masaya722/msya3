m = int(input())
a = [list(map(int, input().split())) for _ in range(m)]
n = int(input())
b = set(tuple(map(int, input().split())) for _ in range(n))
x0, y0 = a[0]
for x1, y1 in b:
    dx = x1 - x0
    dy = y1 - y0
    if all((x + dx, y + dy) in b for x, y in a):
        print(dx, dy)
        break
