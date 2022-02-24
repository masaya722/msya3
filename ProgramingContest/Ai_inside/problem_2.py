# 2

# 実行環境
# python 3.8.8

import math

# 素数判定
def get_prime_num_judge(n):
    is_primes = [True for i in range(n+1)]
    is_primes[0] = False
    is_primes[1] = False
    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if is_primes[i]:
            for j in range(2*i, n+1, i):
                is_primes[j] = False
    return is_primes

# 素数列挙
def get_prime_list(n):
    prime_list = []
    is_primes = get_prime_num_judge(n)
    for i in range(len(is_primes)):
        if is_primes[i]:
            prime_list.append(i)
    return prime_list

# m進数取得
def get_m_ary_number(prime_num):
    m_ary_nums = []
    while prime_num != 0:
        m_ary_nums.append(str(prime_num % m))
        prime_num //= m
    return m_ary_nums


n = int(input())
m = int(input())

prime_list = get_prime_list(n)
for prime_num in prime_list:
    if prime_num < 10:
        continue
    m_ary_nums = get_m_ary_number(prime_num)
    if m_ary_nums == list(reversed(m_ary_nums)):
        print(''.join(m_ary_nums))
