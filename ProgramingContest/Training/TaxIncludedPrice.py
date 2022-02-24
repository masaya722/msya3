t,N = map(int,input().split())

def f(a):
    return (100+t)*a//100

ok = 0
ng = 100*N

while ok+1 <ng:
    x = (ok+ng)//2
    if f(x)-x<N:
        ok = x
    else:
        ng = x

ans = f(ok)+1
print(ans)