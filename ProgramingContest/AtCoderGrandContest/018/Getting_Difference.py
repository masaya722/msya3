import math
from functools import reduce

def my_gcd(*numbers):
    return reduce(math.gcd, numbers)

N,K = map(int,input().split())
A =list(map(int,input().split()))
if max(A)<K:
    print("IMPOSSIBLE")
    exit()
flag = False
gd = my_gcd(*A)
if  gd!= 1:
    if K%gd==0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
    exit()
    
even = 0
odd = 0
for a in A:
    if a%2==0:
        odd +=1
    if a%2 ==1:
        even+=1
if odd ==N:
    if K%2 ==0:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')
elif even==N:
    if K%2 ==0:
        print('IMPOSSIBLE')
    else:
        print('POSSIBLE')
else:
    print('POSSIBLE')
