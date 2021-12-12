A, B, C = map(int, input().split())

for i in range(101):
    for j in range(101):
        if A*i-C == B*j:
            print("YES")
            exit()
print("NO")