N = int(input())

z = 0

for i in range(1, 555555 + 1):
    si = str(i)
    ok = True
    for j in si:
        if j != si[0]:
            ok = False

    if ok:
        z +=1
    if z ==N:
        print(i)