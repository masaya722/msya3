N = int(input())
P = [0] + list(map(int, input().split()))

sumP = sum(P)
exist = []
for _ in range(N + 1):
    exist.append([False] * (sumP + 1))
exist[0][0] = True

for i in range(1, N + 1):
    for j in range(sumP + 1):
        if exist[i - 1][j]:
            exist[i][j] = True
        if j >= P[i] and exist[i - 1][j - P[i]]:
            exist[i][j] = True

count = 0
for ok in exist[N]:
    if ok:
        count += 1

print(count)
