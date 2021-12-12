X = int(input())
for i in range(-501,501):
    while i**5<10**9:
        for j in range(-501,i):
            if X == i**5-j**5:
                print(i,j)
                exit()
        break