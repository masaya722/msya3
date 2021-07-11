import math
A,B,C,D = map(int,input().split())

A -=1
def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)

lcm = my_lcm(C,D)

ans = (B-(B//D+B//C-B//lcm))-(A-(A//C+A//D-A//lcm))
print(ans)