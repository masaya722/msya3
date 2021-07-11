from collections import deque
H,W = map(int,input().split())
N = int(input())
A = list(map(int,input().split()))
colors = []
for i,a in enumerate(A):
    i+=1
    for _ in range(a):
        colors.append(i)

left_corner =False
row = []
for i,color in enumerate(colors):
    i+=1
    row.append(color)
    if i%W ==0:
        if left_corner:
            row.reverse()
            print(*row)
        else:
            print(*row)
        left_corner = not left_corner
        row.clear()
    