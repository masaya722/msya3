from collections import defaultdict as dd
import bisect as bi
import sys
sys.setrecursionlimit(10**8)

N = int(input())
P = list(map(int,input().split()))
edge = dd(list)
for i in range(N-1):
    edge[P[i]].append(i+2)

depth =[-1]*(N+1)
depth[1] = 0
depthList = dd(list)
incnt = [-1]*(N+1)
outcnt = [-1]*(N+1)
cnt = 0

def dfs(k):
    global cnt
    global edge
    incnt[k] = cnt
    depthList[depth[k]].append(cnt)
    cnt +=1

    for i in edge[k]:
        if depth[i] != -1:
            continue
        depth[i] = depth[k]+1
        dfs(i)
    outcnt[k] = cnt
    cnt +=1
dfs(1)

Q = int(input())
for i in range(Q):
    U,D = map(int,input().split())
    ans = bi.bisect_right(depthList[D],outcnt[U])- bi.bisect_left(depthList[D],incnt[U])
    print(ans)
