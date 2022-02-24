from itertools import groupby
S = input()
K = int(input())
a = [sum(1 for _ in g)for _,g in groupby(S)]

if len(a) == 1:
    print(a[0]*K//2)
else:
    ans = sum(x//2*K for x in a)
    if S[0] ==S[-1]:
        ans += ((a[0]+a[-1])//2 -a[0]//2 -a[-1]//2)*(K-1)
    print(ans)