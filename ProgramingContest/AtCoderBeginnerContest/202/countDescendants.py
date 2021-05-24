from collections import defaultdict as dd
import bisect as bi

N = int(input())
P = list(map(int, input().split()))
edge = dd(list)
for k, v in enumerate(P):
    edge[v].append(k+2)

depth = [-1]*(N+1)
depth[1] = 0
depthList = dd(list)
cnt = 0
incnt = [-1]*(N+1)
outcnt = [-1]*(N+1)
f = dd(lambda: dd(int))


def dfs(k):
    global cnt
    global edge
    incnt[k] = cnt
    depthList[depth[k]].append(cnt)
    cnt += 1

    for i in edge[k]:
        if depth[i] != -1:
            continue
        depth[i] = depth[k]+1
        dfs(i)
    outcnt[k] = cnt
    cnt += 1


dfs(1)

Q = int(input())
for _ in range(Q):
    U, D = map(int, input().split())
    ans = bi.bisect_right(depthList[D], outcnt[U]) - \
        bi.bisect_left(depthList[D], incnt[U])
    print(ans)