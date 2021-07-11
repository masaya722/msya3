A,K = map(int,input().split())
money = A
count =0
if K==0:
    print(2*10**12-A)
else:
    while True:
        money += 1+K*money
        count +=1
        if money >=2*(10**12):
            print(count)
            break

