import math
from bisect import bisect_left

def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False

    return prime
prime_numbers = sieve_of_eratosthenes(10**5)
primes = []
for i in range(len(prime_numbers)):
    if prime_numbers[i] and prime_numbers[(i+1)//2]:
        primes.append(i)
Q = int(input())
for i in range(Q):
    l,r = map(int,input().split())
    ans = 0
    for pr in primes:
        if l<=pr<=r:
            ans+=1
        elif r<pr:
            break
    print(ans)
