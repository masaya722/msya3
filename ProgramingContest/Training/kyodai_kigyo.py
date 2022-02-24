import sys

sys.setrecursionlimit(1000000)

N = int(input())

edges = []
for _ in range(N):
    edges.append([])

R = -1
for i in range(N):
    p = int(input())
    if p == -1:
        R = i
    else:
        edges[p - 1].append(i)

queries = []
for _ in range(N):
    queries.append([])

Q = int(input())
for i in range(Q):
    a, b = map(int, input().split())
    queries[a - 1].append((i, b - 1))

ans = [False] * Q
boss = [False] * N


def dfs(i):
    for q, b in queries[i]:
        ans[q] = boss[b]
    boss[i] = True
    for j in edges[i]:
        dfs(j)
    boss[i] = False


dfs(R)

for i in range(Q):
    if ans[i]:
        print("Yes")
    else:
        print("No")
