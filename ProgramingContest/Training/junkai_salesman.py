N = int(input())
A = []
for _ in range(N):
    a = list(map(int, input().split()))
    A.append(a)

ALL = 1 << N
cost = []
INF = 10 ** 20
for _ in range(ALL):
    cost.append([INF] * N)
cost[0][0] = 0


def has_bit(n, j):
    return n & (1 << j) > 0


for n in range(ALL):
    for i in range(N):
        for j in range(N):
            if i == j or has_bit(n, j):
                continue

            cost[n | 1 << j][j] = min(cost[n | 1 << j][j], cost[n][i] + A[i][j])
ans = cost[ALL - 1][0]
print(ans)
