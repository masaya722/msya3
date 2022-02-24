N, M = map(int, input().split())
S = [0]
C = [0]
for i in range(M):
    s, c = input().split()
    s_val = 0
    for j in range(N):
        if s[j] == 'Y':
            s_val += 1 << j
    S.append(s_val)
    C.append(int(c))

ALL = 1 << N

cost = []
INF = 10 ** 100
for _ in range(M + 1):
    cost.append([INF] * ALL)

cost[0][0] = 0

for i in range(1, M + 1):
    for j in range(ALL):
        cost[i][j] = min(cost[i][j], cost[i - 1][j])

        cost[i][j | S[i]] = min(cost[i][j | S[i]], cost[i - 1][j] + C[i])

ans = cost[M][ALL-1]
if ans ==INF:
    ans =-1
print(ans)