S = list(input())


count =0
for i in range(10000):
    a = [0 for _ in range(10)]
    flag = True
    for _ in range(4):
        x = i%10
        a[x] = 1
        i //=10
    for j in range(10):
        if S[j] == 'o' and a[j] != 1:
            flag = False
            break
        if S[j] == 'x' and a[j] != 0:
            flag = False
            break
    if flag:
        count +=1
print(count)