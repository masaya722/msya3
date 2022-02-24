from bisect import bisect_left


N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))

pos = [0 for _ in range(N+1)]
for i in range(N):
    pos[Q[i]] = i
z = [10**9 for _ in range(N)]
for p in P:
    ls = []
    for j in range(p,N+1,p):
        ls.append(pos[j])
    ls.sort(reverse=True)
    for l in ls:
        z[bisect_left(z,l)] = l
print(bisect_left(z,10**9))