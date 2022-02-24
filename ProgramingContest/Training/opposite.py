import math
N = int(input())
x0,y0 = map(int,input().split())
xn2,yn2 = map(int,input().split())

p,q = (x0+xn2)/2,(y0+yn2)/2

theta = math.pi*2/N
x1 = math.cos(theta)*(x0-p)-math.sin(theta)*(y0-q)+p
y1 = math.sin(theta)*(x0-p)+math.cos(theta)*(y0-q)+q
print(x1,y1)