import sys
sys.setrecursionlimit(10**8)

N,M=map(int,input().split())

cities = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    cities[a-1].append(b-1)

done = [False]*N
def dfs(i):
    global done
    global cities
    if done[i]:
        return
    done[i] = True
    for c in cities[i]:
        dfs(c)
    return

total = 0
for i in range(N):
    dfs(i)
    total += sum(done)
    done = [False]*N
print(total)
