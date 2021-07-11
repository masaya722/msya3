N =int(input())
S =[]
for i in range(N):
    s = input()
    S.append(s)

count = 0
for i in range(9):
    circle = 0
    for j in range(N):
        if S[j][i] =='x':
            count+=1
        elif S[j][i] =='o':
            if j>0 and S[j-1][i] !='o':
                circle +=1
            elif j ==0:
                circle +=1
    count +=circle
print(count)        