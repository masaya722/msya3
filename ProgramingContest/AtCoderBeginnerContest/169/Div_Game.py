def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

from collections import defaultdict
N = int(input())
pf = prime_factorize(N)
dict = defaultdict(int)
for i in pf:
    dict[i]+=1

ans = 0
for i,j in dict.items():
    cnt = j
    for k in range(1,50):
        if k<=cnt:
            cnt-=k
            ans+=1
print(ans)