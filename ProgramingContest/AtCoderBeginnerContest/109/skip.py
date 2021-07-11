import math
N,X = map(int,input().split())
x = list(map(int,input().split()))

diff = [abs(X-i) for i in x]
if N ==1:
    print(abs(x[0]-X))
else:
    ans = math.gcd(diff[0],diff[1])
    for i in range(2,len(diff)-1):
        ans = math.gcd(diff[i],ans)
    print(ans)
