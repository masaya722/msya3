from collections import defaultdict as dd
import bisect as bi
from sys import setrecursionlimit
setrecursionlimit(10**8)

N = int(input())
P = list(map(int, input().split()))
edge = dd(list)
for k, v in enumerate(P):
    edge[v].append(k+2)

depth = [-1]*(N+1)
depth[1] = 0
depth_list = dd(list)
cnt = 0
incnt = [-1]*(N+1)
outcnt = [-1]*(N+1)


def dfs(k):
    global cnt
    global edge
    incnt[k] = cnt
    depth_list[depth[k]].append(cnt)
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
    ans = bi.bisect_right(depth_list[D], outcnt[U]) - \
        bi.bisect_left(depth_list[D], incnt[U])
    print(ans)