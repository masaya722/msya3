import sys
import itertools

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())

edges = []
for _ in range(N):
    edges.append([False] * N)
for _ in range(M):
    x, y = map(int, input().split())
    edges[x - 1][y - 1] = True
    edges[y - 1][x - 1] = True



ans = 0


def dfs(i, group):
    global ans
    if i == N:
        flag = True
        for j, k in itertools.combinations(group, 2):
            if not edges[j][k]:
                flag = False
                break
        if flag:
            ans = max(ans, len(group))
    if i < N:
        dfs(i + 1, group)
        dfs(i + 1, group + [i])


dfs(0, [])

print(ans)
