N = int(input())
x = list(map(int,input().split()))
sort_x = sorted(x)
for i in range(N):
    median1 = sort_x[(N+1)//2-1]
    median2 = sort_x[(N+1)//2]
    if x[i]>median1 or x[i] == median2:
        print(median1)
    elif x[i]<median2 or x[i] == median1:
        print(median2)