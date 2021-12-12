from collections import defaultdict
N = int(input())
S = input()

cnt = defaultdict(int)
for s in S:
    cnt[s]+=1
ans = 1
MOD = 10**9+7
for i in cnt.values():
    ans*=(i+1)
    ans%=MOD
print(ans-1)