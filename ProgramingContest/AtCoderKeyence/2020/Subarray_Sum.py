N,K,S =map(int,input().split())
A= []
for _ in range(K):
    A.append(S)
if S != 10**9:
    for _ in range(N-K):
        A.append(S+1)
else:
    for _ in range(N-K):
        A.append(S-1)
print(*A)