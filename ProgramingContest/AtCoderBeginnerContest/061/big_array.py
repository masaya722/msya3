N,K = map(int,input().split())

pre_sort =[]
for i in range(N):
    a,b = map(int,input().split())
    pre_sort.append((a,b))

aft_sort = sorted(pre_sort)

for i,j in aft_sort:
    K -=j
    if K<=0:
        print(i)
        break