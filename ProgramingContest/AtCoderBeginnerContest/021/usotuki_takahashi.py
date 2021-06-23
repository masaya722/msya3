from typing import Set


N =int(input())
a,b = map(int,input().split())
K = int(input())
P =list(map(int,input().split()))

if a in P or b in P:
    print("NO")
else:
    if len(P) != len(set(P)):
        print("NO")
    else:
        print("YES")