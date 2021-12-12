N,K,M,R =map(int,input().split())
S = []
for i in range(N-1):
    S.append(int(input()))

S.sort(reverse=True)

if sum(S[0:K])/K >= R:
    print(0)
else:
    ans = R*K -sum(S[0:K-1])
    if ans >M:
        print(-1)
    else:
        print(ans)