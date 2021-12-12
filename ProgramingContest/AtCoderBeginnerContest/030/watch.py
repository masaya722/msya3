n,m = map(int,input().split())
n%=12
n*=30
n+=0.5*m
m*=6
ans = min(abs(n-m),abs(m-n))
if ans>180:
    print(360-ans)
else:
    print(ans)