B, C = map(int, input().split())

if C ==1:
    if B == 0:
        print(1)
    else:
        print(2)
    exit()

upper1 = B + (C-2)//2
lower1 = B -C//2
upper2 = -B+(C-1)//2
lower2 = -B-(C-1)//2

if B>0:
    ans = (upper1 -lower1 +1) +(upper2-lower2+1) -max(upper2-lower1+1,0)
else:
    ans = (upper1 -lower1 +1) +(upper2-lower2+1) -max(upper1-lower2+1,0)
print(ans)