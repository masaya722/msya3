from collections import defaultdict
N = int(input())
T = []
for i in range(N):
    T.append(int(input()))
T.sort()
sumt = [0]
for i in range(N):
    sumt.append(T[i]+sumt[-1])
cnt = defaultdict(int)

for i in range(N):
    cnt[T[i]]+=1
ans = 1
MOD = 10**9+7
for cv in cnt.values():
    if cv >1:
        for i in range(2,cv+1):
            ans*=i
            ans%=MOD
print(sum(sumt))
print(ans%MOD)
