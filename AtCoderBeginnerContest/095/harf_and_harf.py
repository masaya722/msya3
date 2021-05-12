a, b, c, x, y = list(map(int, input().split()))

value = 10 ** 18
for i in range(10 ** 5 + 1):
    if i>x and i>y:
        break
    A = max(0, x - i)
    B = max(0, y - i)
    value = min(value, A*a+B*b+2*c*i)
print(value)
