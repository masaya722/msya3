X,Y,W = input().split()
x = int(X)-1
y =int(Y)-1
C = []
for i in range(9):
    C.append(input())

ans = ''
flag_row = False 
flag_cal = False 
while len(ans)<4:
    ans+=C[y][x]
    if 'R' in W:
        if x ==8:
            flag_row = True
        if flag_row:
            x-=1
        else:
            x+=1
    if 'L' in W:
        if x==0:
            flag_row = True
        if flag_row:
            x+=1
        else:
            x-=1
    if 'D' in W:
        if y==8:
            flag_cal = True
        if flag_cal:
            y-=1
        else:
            y+=1
    if 'U' in W:
        if y==0:
            flag_cal = True
        if flag_cal:
            y+=1
        else:
            y-=1
print(ans)
