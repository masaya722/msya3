N = int(input())
X = list(map(int,input().split()))
prime_nums = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
ans = []
for i in range(2**15):
    temp = 1
    for j in range(15):
        if i>>j&1:
            temp*=prime_nums[j]
    ans.append(temp)
ans.sort()

import math
for a in ans:
    if a ==1:
        continue
    flag = True
    for x in X:
        if math.gcd(a,x) ==1:
            flag =False
    if flag:
        print(a)
        exit()
print(X[0])
