T = int(input())
for t in range(T):
    r,g,b = map(int,input().split())
    tmpr = r
    tmpg = g
    tmpb = b
    diff1 = abs(r-b)
    diff2 = abs(g-b)
    diff3 = abs(r-g)
    if diff1%3 !=0 and diff2%3 !=0 and diff3%3 !=0:
        print(-1)
        continue
    ans = 10**18
    if diff1%3 ==0:
        cnt =0
        plus = diff1//3
        g-=plus
        r=(plus+b+r)//2
        b=(plus+b+r)//2
        cnt=plus+r
        ans = min(ans,cnt)
    r = tmpr
    g = tmpg
    b = tmpb
    if diff2%3 ==0:
        cnt =0
        plus = diff2//3
        r-=plus
        g=(plus+g+b)//2
        b=(plus+g+b)//2
        cnt=plus+g
        ans = min(ans,cnt)
    r = tmpr
    g = tmpg
    b = tmpb
    if diff3%3 ==0:
        cnt =0
        plus = diff3//3
        b-=plus
        r=(plus+r+g)//2
        g=(plus+r+g)//2
        cnt=plus+r
        ans = min(ans,cnt)
    print(ans)
