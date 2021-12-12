import sys
sys.setrecursionlimit(10**6)
N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

edges = [[]for _ in range(N)]
for i in range(M):
    c,d = map(int,input().split())
    c -=1
    d -=1
    edges[c].append(d)
    edges[d].append(c)
done = [False for _ in range(N)]
total_a = 0
total_b = 0
def dfs(i):
    global total_a
    global total_b
    if done[i]:
        return
    done[i] = True
    total_a +=A[i]
    total_b +=B[i]
    for j in edges[i]:
        dfs(j)
    return
for i in range(N):
    dfs(i)
    if total_a !=total_b:
        print("No")
        exit()
    total_a = 0
    total_b = 0
print("Yes")
