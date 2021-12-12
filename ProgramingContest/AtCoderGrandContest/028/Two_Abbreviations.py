import math
from collections import defaultdict
def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)
n,m = map(int,input().split())
l = my_lcm(n,m)
S = input()
T = input()
dict = defaultdict(int)
for i in range(n):
    dict[l//n*i]+=1
for i in range(m):
    dict[l//m*i]+=1

temp = []
for i,j in dict.items():
    if j ==2:
        temp.append(i)
for i in temp:
    if S[i//(l//n)] != T[i//(l//m)]:
        print(-1)
        exit()
print(l)
