N = int(input())
A =list(map(int,input().split()))
up = False
down = False
count = 1
for i in range(N-1):
    if not up and not down:
        if A[i]<A[i+1]:
            up = True
        elif A[i]>A[i+1]:
            down = True
    elif up and A[i]>A[i+1]:
        up = False
        count+=1
    elif down and A[i]<A[i+1]:
        down = False
        count+=1
print(count) 
