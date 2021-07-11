import math

N = int(input())
x, y = map(int, input().split())
x2, y2 = map(int, input().split())
p, q = (x+x2)/2, (y+y2)/2
theta = 360/N

a = (x-p)*math.cos(math.radians(theta)) - (y-q)*math.sin(math.radians(theta))+p
b = (x-p)*math.sin(math.radians(theta))+(y-q)*math.cos(math.radians(theta))+q
print(a,b)
print(math.radians(theta))