from bisect import bisect_left

n =int(input())
a = list(map(int,input().split()))
a.sort()
if n ==2:
    print(a[1],a[0])
    exit()
first = a[n-1]
idx = bisect_left(a,first//2)
second = 0
if idx ==0:
    second= a[idx]
elif abs(a[idx]-first//2)>abs(a[idx-1]-first//2):
    second = a[idx-1]
else:
    second = a[idx]
print(first,second)
