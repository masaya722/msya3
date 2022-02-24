N = int(input())
R = list(map(int,input().split()))
up = True
down = True
cnt = 1
for i in range(N-1):
    if down and R[i]<R[i+1]:
        cnt+=1
        up = True
        down = False
    elif up and R[i]>R[i+1]:
        cnt+=1
        down = True
        up = False
    else:
        continue
if cnt <3:
    print(0)
else:
    print(cnt)