N, L = list(map(int, input().split()))
X = list(map(int, input().split()))
T1, T2, T3 = list(map(int, input().split()))

H = [False] * (L + 1)
for x in X:
    H[x] = True

cost = [10 ** 100] * (L + 1)

cost[0] = 0

for i in range(1, L + 1):
    cost[i] = min(cost[i], cost[i - 1] + T1)
    if i >= 2:
        cost[i] = min(cost[i], cost[i - 2] + T1 + T2)
    if i >= 4:
        cost[i] = min(cost[i], cost[i - 4] + T1 + 3 * T2)
    if H[i]:
        cost[i] += T3

ans = cost[L]
for i in [L - 3, L - 2, L - 1]:
    if i >= 0:
        ans = min(ans, cost[i] + T1 // 2 + T2 * (2 * (L - 1) - 1) // 2)
print(ans)
