n = int(input())
use = n+1
count = 0
ok = n+1
ng = 0
while ok-ng>1:
    mid = (ok+ng)//2
    if (1+mid)*mid//2 <=use:
        ng = mid
    else:
        ok = mid
print(n+1-ng) 
