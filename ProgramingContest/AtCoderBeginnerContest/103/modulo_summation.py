import math
from functools import reduce

N = int(input())
A = list(map(int,input().split()))
def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def my_lcm(*numbers):
    return reduce(my_lcm_base, numbers, 1)

S = my_lcm(*A)-1
total =0
for a in A:
    total+=S%a
print(total)