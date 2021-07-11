from itertools import groupby

s = input()
k = int(input())
a = [sum(1 for _ in g) for _,g in groupby(s)]

if len(a) ==1:
    print(len(s)*k//2)
else:
    ans = sum(x//2*k for x in a)
    if s[0] == s[-1]:
        ans += ((a[0]+a[-1])//2 -a[0]//2 -a[-1]//2)*(k-1)
    print(ans)