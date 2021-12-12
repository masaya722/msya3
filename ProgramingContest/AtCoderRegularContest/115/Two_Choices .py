from collections import defaultdict
n,m = map(int,input().split())

s_count = []
for i in range(n):
    s = input()
    s_count.append(s.count('1')%2)

x = s_count.count(1)
y = s_count.count(0)
print(x*y)
