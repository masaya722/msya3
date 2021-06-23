N = int(input())
BA = []
for _ in range(N):
    a, b = map(int, input().split())
    BA.append([b, a])
BA.sort()

last = 0

count = 0
for b, a in BA:
    if a > last:
        last = b
        count += 1

print(count)