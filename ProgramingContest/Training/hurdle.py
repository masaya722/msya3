N, L = map(int, input().split())
X = list(map(int, input().split()))
t1, t2, t3 = map(int, input().split())

hurdle = [False] * (L + 1)

for x in X:
    hurdle[x] = True

cost = [10 ** 10] * (L + 1)
cost[0] = 0

for i in range(1, L + 1):
    cost[i] = min(cost[i], cost[i - 1] + t1)
    if i >= 2:
        cost[i] = min(cost[i], cost[i - 2] + t1 + t2)
    if i >= 4:
        cost[i] = min(cost[i], cost[i - 4] + t1 + 3 * t2)
    if hurdle[i]:
        cost[i] += t3

ans = cost[L]
for i in [L - 1, L - 2, L - 3]:
    ans = min(ans, cost[i] + t1//2 + t2*((L - i) * 2 - 1) // 2)
print(ans)
