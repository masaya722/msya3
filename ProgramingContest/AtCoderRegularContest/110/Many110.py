N = int(input())
t = input()
T = [int(i) for i in t]
if t == '1':
    print(2*(10**10))
elif t =='11':
    print(10**10)
else:
    flag = False
    first_zero = 0
    for num,i in enumerate(T):
        if i ==0:
            flag = True
            first_zero = num
        if not flag and num ==2:
            print(0)
            exit()
        if flag:
            break
    tmp2 =[]
    for i in range(N):
        if i%3 ==first_zero:
            tmp2.append(0)
        else:
            tmp2.append(1)
    if T !=tmp2:
        print(0)
        exit()
    else:
        if first_zero ==0:
            print((3*(10**10)-2-N)//3+1)
        elif first_zero ==1:
            print((3*(10**10)-1-N)//3+1)
        else:
            print((3*(10**10)-N)//3+1)


