import math

txa,tya,txb,tyb,T,V = map(int,input().split())
n = int(input())

total =  T*V
flag = False
for i in range(n):
    x,y =map(int,input().split())
    if math.sqrt((txa -x)**2+(tya-y)**2)+math.sqrt((txb -x)**2+(tyb-y)**2) <= total:
        flag = True
if flag:
    print("YES")
else:
    print("NO")