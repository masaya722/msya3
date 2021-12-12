N,K = map(int,input().split())
K = abs(K)
if K<N:
    p = K+1
else:
    p = 2*N -K-1
q = 1
ans = 0
rev1 = False
rev2 = False
for i in range(2*N-K):
    if K>=N:
        rev1 = True
    ans+=p*q
    if p >=N:
        rev1 = True
    if q >= N:
        rev2 = True
    if rev1:
        p-=1
    else:
        p+=1
    if rev2:
        q-=1
    else:
        q+=1
print(ans)