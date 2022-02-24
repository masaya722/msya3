from bisect import bisect_left
N = int(input())
sums = [0]
for i in range(1,N+1):
    sums.append(sums[i-1]+i)

idx = bisect_left(sums,N)
if sums[idx] ==N:
    for i in range(1,idx+1):
        print(i)
else:
    for i in range(1,idx+1):
        if sums[idx]-N ==i:
            continue
        print(i)