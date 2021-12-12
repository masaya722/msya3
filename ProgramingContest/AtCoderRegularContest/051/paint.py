import math
x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())
red = [x1-r, y1-r, x1+r, y1+r]
if x1-r >= x2 and y1-r >= y2 and x1+r <= x3 and y1+r <= y3:
    if math.sqrt((x1-x2)**2+(y1-y2)**2) > r and math.sqrt((x1-x2)**2+(y1-y3)**2) > r\
            and math.sqrt((x1-x3)**2+(y1-y2)**2) > r and math.sqrt((x1-x3)**2+(y1-y3)**2) > r:
            print('NO')
            print('YES')
            exit()
elif math.sqrt((x1-x2)**2+(y1-y2)**2) <= r and math.sqrt((x1-x2)**2+(y1-y3)**2) <= r\
            and math.sqrt((x1-x3)**2+(y1-y2)**2) <= r and math.sqrt((x1-x3)**2+(y1-y3)**2) <= r:
            print('YES')
            print('NO')
            exit()
print('YES')
print('YES')