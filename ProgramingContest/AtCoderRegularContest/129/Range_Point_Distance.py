n = int(input())
L = []
R = []
for i in range(n):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
maxl = 0
minr = 10**18
for i in range(n):
    maxl = max(maxl, L[i])
    minr = min(minr, R[i])
    if minr >= maxl:
        print(0)
    else:
        x = (maxl+minr)//2
        print(max(maxl-x,x-minr,0))
