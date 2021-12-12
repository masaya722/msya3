N = int(input())
a = list(map(int,input().split()))

suma = sum(a)
if suma%N !=0:
    print(-1)
else:
    meana =suma//N
    total =0
    count = 0
    ans = 0
    for i,num in enumerate(a):
        total+=num
        if total ==meana*(i+1-count):
            ans +=i-count
            count=i+1
            total =0
    print(ans)
