N = int(input())
A = list(map(int,input().split()))
ans = 1<<30
for i in range(1<<(N-1)):
    aft_xor = 0
    bef_xor = 0
    for j in range(N):
        bef_xor |=A[j]
        if i>>j&1:
            aft_xor^=bef_xor
            bef_xor =0
    aft_xor^=bef_xor
    ans = min(ans,aft_xor)
print(ans)