from collections import defaultdict
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

N =int(input())

cnt = defaultdict(int)
for i in range(1,N+1):
    for j in prime_factorize(i):
        cnt[j]+=1

ans = 1
MOD = 10**9+7
for num in cnt.values():
    ans*=num+1
    ans%=MOD
print(ans%MOD)

