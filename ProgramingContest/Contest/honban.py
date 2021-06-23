import sys
sys.setrecursionlimit(10**8)
N = int(input())
A = list(map(int, input().split()))

s = N//2
edge = [[] for _ in range(2*10**5+1)]
done = [False]*(2*10**5+1)
S = []
for i in range(s):
    if A[i] != A[-i-1]:
        edge[A[i]].append(A[-i-1])
        edge[A[-i-1]].append(A[i])

setA = set(A)

count =0
flag = False
def dfs(i):
    global count
    global flag
    if done[i]:
        return
    done[i] = True
    if flag:
        count+=1
    for j in edge[i]:
        flag = True
        dfs(j)
    return

for i in setA:
    dfs(i)
    flag =False

print(count)