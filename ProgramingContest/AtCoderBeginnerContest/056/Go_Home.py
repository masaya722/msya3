X = int(input())
total = 0
for i in range(1,X+1):
    total+=i
    if total>=X:
        print(i)
        exit()