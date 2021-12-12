import math
def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)
N = int(input())
T = []
for i in range(N):
    T.append(int(input()))
ans = 1
for t in T:
    ans = my_lcm(ans,t)
print(ans)

