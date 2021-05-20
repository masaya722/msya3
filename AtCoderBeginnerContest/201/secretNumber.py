import itertools
s = input()
ans = 0
for num in range(0, 10000):
    a = [0 for _ in range(10)]
    x = num
    for i in range(0, 4):
        d = x % 10
        a[d] = 1
        x //= 10
    ok = True
    for i in range(0, 10):
        if s[i] == 'o' and a[i] != 1:
            ok = False
        if s[i] == 'x' and a[i] != 0:
            ok = False
    if ok:
        ans +=1
print(ans)
