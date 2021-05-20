N = int(input())

R = []
for _ in range(N):
    x, l = map(int, input().split())
    R.append((l + x, x - l))

R.sort()
count = 0
length = -10**9
for i, j in R:
    if length <= j:
        length = i
        count += 1
print(count)