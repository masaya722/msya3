n, q = map(int, input().split())
graph = []
for _ in range(n):
    row = []
    for _ in range(n):
        row.append(False)
    graph.append(row)

for _ in range(q):
    s = list(map(int, input().split()))
    a = s[1]
    if s[0] == 1:
        b = s[2]
        graph[a - 1][b - 1] = True
    elif s[0] == 2:
        for i in range(n):
            if graph[i][a - 1]:
                graph[a - 1][i] = True
    elif s[0] == 3:
        to_follow = []
        for i in range(n):
            if graph[a - 1][i]:
                for j in range(n):
                    if graph[i][j] and j != a-1:
                        to_follow.append(j)
        for i in to_follow:
            graph[a-1][i] = True

for i in range(n):
    for j in range(n):
        if graph[i][j]:
            print("Y", end="")
        else:
            print("N", end="")
    print()
