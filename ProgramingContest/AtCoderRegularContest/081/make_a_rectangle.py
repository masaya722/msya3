import bisect

N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
A.append(0)
x = 0
cnt =1
use = []
for a in A:
    if x ==a:
        cnt +=1
    else:
        if cnt >=2:
            use.append((x,cnt))
            cnt = 1
    x = a

max = 0
if use != []:
    a,cnt = use[0]
    if cnt>=4:
        print(a*a)
        exit()
    elif len(use)>=2:
        a1,cnt1 =use[1]
        print(a1*a)
        exit()
print(0)