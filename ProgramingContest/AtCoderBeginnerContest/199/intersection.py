n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = []

for i in range(a[0], b[0] + 1):
    x.append(i)
for i in range(1, n):
    remove_x =[]
    for k in x:
        if a[i] <= k <= b[i]:
            continue
        else:
            remove_x.append(k)
    for k in remove_x:
        x.remove(k)

print(len(x))
