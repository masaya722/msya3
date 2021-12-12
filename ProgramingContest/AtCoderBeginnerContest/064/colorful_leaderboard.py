N = int(input())
a = list(map(int,input().split()))

count =0
color = []
for i in range(N):
    if a[i]>=3200:
        count+=1
    else:
        color.append(a[i]//400)

ans = len(set(color))
if ans ==0:
    print(1,count)
else:
    print(ans,ans+count)

