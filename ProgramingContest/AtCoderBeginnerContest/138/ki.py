from typing import DefaultDict
import sys
sys.setrecursionlimit(10**8)

N,Q= map(int,input().split())
tree = [[]for _ in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    a -=1
    b -=1
    tree[a].append(b)
    tree[b].append(a)

dict = DefaultDict(int)
for i in range(Q):
    p,x = map(int,input().split())
    p-=1
    dict[p] +=x
count = [0]*N
done = [False]*N
def dfs(root):
    global count
    global done
    if done[root]:
        return
    done[root] = True
    count[root]+=dict[root]
    for i in tree[root]:
        if not done[i]:
            count[i]+=count[root]
        dfs(i)
    return
dfs(0)
for i in range(N):
    if i !=N-1:
        print(count[i],end=" ")
    else:
        print(count[i])
