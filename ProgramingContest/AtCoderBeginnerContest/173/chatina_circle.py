N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

s = N-1
count = 0
total = 0
while s > 0:
    if count == 0:
        total += A[count]
        s -= 1
    elif s > 1:
        total += A[count]*2
        s -= 2
    else:
        total += A[count]
        s -= 1
    count += 1
print(total)
