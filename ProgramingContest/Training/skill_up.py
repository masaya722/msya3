N, M, X = list(map(int, input().split()))

books = []
for i in range(N):
    lst = list(map(int, input().split()))
    books.append(lst)

ALL = 1 << N
cost = [0]*ALL
skillScore =[]
for i in range(ALL):
    skillScore.append([0] * M)

for n in range(ALL):
    for i in range(0, N):
        if n & (1 << i) > 0:
            for j in range(M):
                skillScore[n][j] += books[i][j + 1]
            cost[n] += books[i][0]

ans = 10 ** 20
for n in range(ALL):
    if min(skillScore[n]) < X:
        continue
    ans = min(ans, cost[n])
if ans ==10**20:
    ans = -1
print(ans)
