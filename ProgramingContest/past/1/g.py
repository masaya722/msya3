from itertools import combinations

N = int(input())
A = []
for i in range(N-1):
    a = [0]*(i+1)+list(map(int,input().split()))
    A.append(a)

ALL = 1<<N

happy = []
def has_bit(i,j):
    return i>>j&1>0

for i in range(ALL):
    tmp = 0
    for j in range(N):
        for k in range(j+1,N):
            if has_bit(i,j) and has_bit(i,k):
                tmp+=A[j][k]
    happy.append(tmp)

ans = -10**100
for a in range(ALL):
    for b in range(ALL):
        if a&b>0:
            continue
        c = ALL-1-(a|b)
        ans =max(ans,happy[a]+happy[b]+happy[c])
print(ans)