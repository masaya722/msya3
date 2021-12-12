# iは素数を探す上限の値
def get_prime_number(n):
    ptr = 0
    prime = [None]*(n//2)
    prime[ptr] = 2
    ptr+=1
    prime[ptr] = 3
    ptr +=1
    prime_numbers = []
    for i in range(5,n+1,2):
        j = 1
        while prime[j]*prime[j]<=i:
            if i%prime[j]==0:
                break
            j+=1
        else:
            prime[ptr] = i
            ptr+=1
    for i in range(ptr):
        prime_numbers.append(prime[i])
    return prime_numbers

