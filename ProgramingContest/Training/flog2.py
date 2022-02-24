n, k = map(int, input().split())
h = list(map(int, input().split()))

cost = [10 ** 20] * n
cost[0] = 0
cost[1] = cost[0] + abs(h[1] - h[0])

for i in range(2, n):
    for j in range(1, k + 1):
        cost[i] = min(cost[i], cost[i - j] + abs(h[i] - h[i - j]))
print(cost[n-1])
