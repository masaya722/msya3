N = int(input())
A = list(map(int,input().split()))
S= []
for i in range(N):
    S.append((A[i],i+1))
S.sort(reverse=True)
for i,j in S:
    print(j)
