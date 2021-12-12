N = list(input())
N.reverse()
tmp1 =0
tmp2 = 0
for i in range(len(N)):
    if i%2 ==0:
        tmp1+=int(N[i])
    else:
        tmp2 +=int(N[i])
print(tmp2,tmp1)