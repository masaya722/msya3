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

N,P = map(int,input().split())
if N ==1:
    print(P)
    exit()
primes = prime_factorize(P)
dict = defaultdict(int)
for p in primes:
    dict[p]+=1
ans = 1
for prm,num in dict.items():
    if num >=N:
        ans*=prm**(num//N)
print(ans)
