s = int(input())
s_digit = len(str(s))

if s ==10**18:
    print(10**9,0,1,10**9,0,0)
elif s_digit>9:
    x1 = 10**9
    y2 = s//x1+1
    x2 = x1*y2-s
    y1 = 1
    print(x1, y1, x2, y2,0,0)
elif s % 2 == 0:
    x1 = (s+2)//2
    y2 = 2
    x2 = 2
    y1 = 1
    print(x1, y1, x2, y2,0,0)
else:
    x1 = (s+1)//2
    y2 = 2
    x2 = 1
    y1 = 1
    print(x1, y1, x2, y2,0,0)
