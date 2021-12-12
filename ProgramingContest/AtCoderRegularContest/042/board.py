N,M = map(int,input().split())
num_list=  [i+1 for i in range(N)]
A = []
for i in range(M):
    A.append(int(input()))
A.reverse()
ans = []
x = [0]*(N+1)
for a in A:
    if x[a] ==0:
        ans.append(a)
        x[a]=1
for i in range(1,N+1):
    if x[i] ==0:
        ans.append(i)
for i in ans:
    print(i)
