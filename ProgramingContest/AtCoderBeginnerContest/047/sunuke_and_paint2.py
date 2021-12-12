W,H,N = map(int,input().split())
INF = 10**18
x1= 0
x2 = INF
y1 = 0
y2 =INF
for i in range(N):
    x,y,a = map(int,input().split())
    if a ==1:
        x1 = max(x,x1)
    elif a ==2:
        x2 = min(x,x2)
    elif a ==3:
        y1 = max(y,y1)
    else:
        y2 = min(y,y2)
if x2 ==INF:
    x2 = W
if y2 == INF:
    y2 = H
if x2-x1<0 or y2 -y1<0:
    print(0)
else:
    print((x2-x1)*(y2-y1))    