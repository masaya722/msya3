n, m, x = list(map(int, input().split()))

a = []

for _ in range(n):
    lst = list(map(int, input().split()))
    a.append(lst)

ans = 10 ** 15
for bit in range(2 ** n):
    M = [0] * m
    cost = 0
    for i in range(n):
        if (bit >> i) & 1:
            cost += a[i][0]
            for j in range(m):
                M[j] += a[i][j + 1]
    flag = True
    for i in range(m):
        if M[i] < x:
            flag = False
    if flag:
        ans = min(ans, cost)
if ans == 10 ** 15:
    ans = -1
print(ans)
