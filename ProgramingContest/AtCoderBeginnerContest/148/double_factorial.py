import sys
sys.setrecursionlimit(10**8)

N= int(input())

def g1(n,p):
    if n<p:
        return 0 
    return n//p +g1(n//p,p)

def g2(n,p):
    if n%2 ==0:
        if p ==2:
            return n//2 +g1(n//2,p)
        else:
            return g1(n//2,p)
    else:
        return 0

ans = min(g2(N,2),g2(N,5))
print(ans)