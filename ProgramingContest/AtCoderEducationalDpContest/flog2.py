n, k = list(map(int, input().split()))
h = [0] + list(map(int, input().split()))
cost = [10 ** 20] * (n + 1)
cost[1] = 0
for i in range(2, n+1):
    for j in range(1, k+1):
        if i - j >= 1:
            cost[i] = min(cost[i], cost[i - j] + abs(h[i] - h[i - j]))
        else:
            break
print(cost[n])
