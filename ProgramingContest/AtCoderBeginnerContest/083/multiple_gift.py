X, Y = map(int, input().split())
a = Y // X
count = 0
while a > 0:
    a = a // 2
    count += 1
print(count)
