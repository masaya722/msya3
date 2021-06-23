import itertools

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append([False] * N)
for i in range(M):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = True
    graph[y - 1][x - 1] = True
ans = 0


def dfs(i, group):
    global ans
    if i == N:
        flag = True

        for i in itertools.combinations(group, 2):
            if not graph[i[0]][i[1]]:
                flag = False
                break
        if flag:
            ans = max(ans, len(group))
    else:
        dfs(i + 1, group)
        dfs(i + 1, group + [i])


dfs(0, [])

print(ans)
