from collections import defaultdict

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

N = int(input())
A = list(map(int,input().split()))

cnt = defaultdict(int)

for a in A:
    cnt[a]+=1

ans = 0
for a in A:
    div_lists = make_divisors(a)
    flag = False
    for dl in div_lists:
        if cnt[dl]==N or (cnt[dl]>0 and dl !=a):
            flag = True
            break
    if not flag:
        ans+=1
print(ans)
