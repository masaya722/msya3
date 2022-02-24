N = int(input())

def g1(n,p):
    if n<p:
        return 0
    return n//p+g1(n//p,p)

def g2(n,p):
    if N%2==0:
        if p==2:
            return N//2+g1(N//2,p)
        elif p ==5:
            return g1(N//2,p)
    else:
        return 0

ans = min(g2(N,2),g2(N,5))
print(ans)