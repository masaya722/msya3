N,M = map(int,input().split())
S = []
for _ in range(M):
    ks = list(map(int,input().split()))[1:]
    S.append(sum(1<<(s-1) for s in ks))

p = list(map(int,input().split()))

ans = 0
for state in range(2**N):
    on =True
    for m in range(M):
        on = bin(S[m]&state).count('1') %2 ==p[m]
        if not on:
            break
    
    ans +=on
print(ans)
