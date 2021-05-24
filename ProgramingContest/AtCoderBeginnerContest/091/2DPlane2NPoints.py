N = int(input())
red = []
for _ in range(N):
    red.append(list(map(int, input().split())))
red.sort(key=lambda x: -x[1])
blue = []
for _ in range(N):
    blue.append(list(map(int, input().split())))
blue.sort()
count = 0
for i, j in red:
    for c, d in blue:
        if i < c and j < d:
            blue.remove([c, d])
            count += 1
            break
print(count)
