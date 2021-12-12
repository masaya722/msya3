N = int(input())
A = list(map(int,input().split()))
MOD = 10**9+7
if N%2==0:
    for i in range(N):
        if A[i]%2==0:
            print(0)
            exit()
else:
    ok = True
    for i in range(N):
        if A[i] ==0:
            if not ok:
                print(0)
                exit()
            ok = False
        if A[i]%2==1:
            print(0)
            exit()
cnt = [0 for _ in range(N)]
for i in range(N):
    cnt[A[i]]+=1
    if cnt[A[i]]>2:
        print(0)
        exit()


ans = 1
for i in range(N//2):
    ans*=2
    ans%=MOD
print(ans)