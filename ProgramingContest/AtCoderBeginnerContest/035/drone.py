from collections import deque
S= input()
T = int(input())

x = S.count("R")-S.count("L")
y = S.count("U")-S.count("D")
absxy = abs(x)+abs(y)
q = S.count("?")

if T==1:
    print(absxy+q)
else:
    if q<absxy:
        print(absxy-q)
    else:
        q -=absxy
        q%=2
        if q==1:
            print(1)
        else:
            print(0)