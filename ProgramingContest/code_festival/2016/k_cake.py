from collections import defaultdict

K,T =map(int,input().split())
A = list(map(int,input().split()))

cnt = defaultdict(int)
ttl = 0
for a in A:
    ttl+=a

max_a = max(A)
if ttl-max_a>=max_a:
    print(0)
else:
    print(max_a-(ttl-max_a)-1)