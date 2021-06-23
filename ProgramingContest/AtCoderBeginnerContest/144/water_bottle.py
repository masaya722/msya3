import math

a, b, x = map(int, input().split())

if x/a > a*b/2:
    h = x*2/(a**2) - b
    ans = math.degrees(math.atan2(b-h, a))

else:
    teihen = x/a*2/b
    ans = math.degrees(math.atan2(b, teihen))
print(ans)
