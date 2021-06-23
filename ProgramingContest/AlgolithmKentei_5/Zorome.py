N = int(input())

# 今まで出てきたゾロ目の数
z = 0

# 1から555555までの整数を全て調べる。調べている数をiとする。
for i in range(1, 555555 + 1):

    si = str(i)

    ok = True

    for s in si:
        if s != si[0]:
            ok =False

    if ok:
        z +=1

    if ok and z == N:
        ans = i
print(ans)